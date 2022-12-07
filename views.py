from flask import Blueprint, render_template, request, redirect, flash
from flask_login import current_user, login_required
from . import db
from .models import Task
from .helpers import format_date, format_time # helper functions
from sqlalchemy import or_

views = Blueprint('views', __name__)



@views.route('/', methods=['POST', 'GET'])
@views.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        # Search Bar
        if request.form['action'] == 'Search':
            print('search!')
            user_query = request.form['Query']
            results = Task.query.filter_by(user_id=current_user.id). \
                                            filter(Task.client.contains(user_query)).all()
            return render_template('home.html', user=current_user, tasks=results, isQuery=True)

        # Optionally hide Completed Tasks
        if request.form['action'] == 'Hide Completed Tasks':
            tasks = Task.query.filter_by(user_id=current_user.id). \
                                    filter(Task.status != 'Completed'). \
                                        order_by(Task.appt_date).all()
            flash('Completed Appointments Hidden!', category='success')
            return render_template('home.html', user=current_user, tasks=tasks, isQuery=False)

        # Optionally delete all Completed and Cancelled Tasks
        if request.form['action'] == 'Clean Up':
            unwanted_tasks = Task.query.filter_by(user_id=current_user.id). \
                                                filter(or_(Task.status == 'Completed', \
                                                            Task.status == 'Cancelled')).all()
            for task in unwanted_tasks:
                db.session.delete(task)
                db.session.commit()
            flash('Completed and Cancelled Appointments Deleted!', category='success')
            remaining_tasks = Task.query.filter_by(user_id=current_user.id). \
                                                    order_by(Task.appt_date_int).all()
            return render_template('home.html', user=current_user, tasks=remaining_tasks, isQuery=False)

        elif request.form['action'] == "Create New":
            return redirect('/create')

    # default action: display all tasks
    tasks = Task.query.filter_by(user_id=current_user.id). \
                                order_by(Task.appt_date_int, Task.time).all()
    return render_template('home.html', user=current_user, tasks=tasks, isQuery=False)



@views.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    if request.method == 'POST':
        if request.form['action'] == 'Add Appointment':
            # Collect data from submitted form
            client = request.form['client']
            appt_date_int = request.form['appt_date']
            time = request.form['time']
            new_time = format_time(time)
            # Parse str object YYYY-MM-DD format, and convert into formatted str
            if len(client.strip()) < 1:
                flash('Client name is too short!', category='error')
            else:
                appt_date = format_date(appt_date_int)
                try:
                    new_task = Task(client=client,
                                    appt_date=appt_date,
                                    appt_date_int=appt_date_int,
                                    time=new_time,
                                    user_id=current_user.id)
                    db.session.add(new_task)
                    db.session.commit()
                    flash('New client added!', category='success')
                    return redirect('/')
                except:
                    flash('Error in adding new client.', category='error')
        elif request.form['action'] == 'Return Home':
            flash('Returning Home!', category='success')
            return redirect('/')
    return render_template('create.html', user=current_user)



@views.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = Task.query.get(id)
    try:
        if task_to_delete.user_id == current_user.id:
            # only owner can delete their Clients
            db.session.delete(task_to_delete)
            db.session.commit()
            flash('Client deleted!', category='success')
            return redirect('/')
    except:
        flash('Error in deleting client.', category='error')



@views.route('/update/<int:id>', methods=['POST', 'GET'])
@login_required
def update(id):
    updated_task = Task.query.get(id)
    if request.method == 'POST':
        if request.form['action'] == 'Return Home':
            flash('Update cancelled. Returning Home!', category='success')
            return redirect('/')

        # Otherwise Update Button submitted
        # and make sure owner only can update
        if updated_task.user_id == current_user.id:
            updated_task.client = request.form['client']
            date_obj = request.form['appt_date']
            updated_task.appt_date = format_date(date_obj)
            updated_task.appt_date_int = date_obj
            if date_obj:
                time = request.form['time']
                updated_task.time = format_time(time)
            else:
                updated_task.time = '' # default time: unspecified/optional
            updated_task.status = request.form.get('taskStatus')
            try:
                db.session.commit()
                flash('Client updated!', category='success')
                return redirect('/')
            except:
                flash('Error in updating client.', category='error')
    else:
        return render_template('update.html', task=updated_task, user=current_user)
