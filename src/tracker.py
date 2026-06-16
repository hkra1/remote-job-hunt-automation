import pandas as pd

def load_tracker(filename='data/applications.csv'):
    try:
        return pd.read_csv(filename)
    except:
        return pd.DataFrame(columns=['job_title', 'company', 'url', 'status', 'date'])

def add_application(tracker, job_title, company, url, status='Applied'):
    new_row = {'job_title': job_title, 'company': company, 'url': url, 'status': status, 'date': pd.Timestamp.now()}
    tracker = pd.concat([tracker, pd.DataFrame([new_row])], ignore_index=True)
    tracker.to_csv('data/applications.csv', index=False)
    return tracker
