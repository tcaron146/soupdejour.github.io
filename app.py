from flask import Flask, render_template, request, redirect
import schedule
import time
import threading

app = Flask(__name__)

def send_weekly_emails():
    # TODO: Implement the code to send emails to all subscribers
    pass

schedule.every().monday.at('09:00').do(send_weekly_emails)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    if request.method == 'POST':
        email = request.form['email']
        # TODO: Remove the email address from the email list
        return redirect('/')
    return render_template('unsubscribe.html')

if __name__ == '__main__':
    # Run the scheduler in a separate thread
    thread = threading.Thread(target=run_scheduler)
    thread.start()

    app.run()
