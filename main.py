#localhost:5000/start?type=A&process=A
from flask import Flask, request
from csv import writer
import time

with open("research_start_logs.csv", mode="w", encoding='utf-8') as research_start_logs:
    file_writer = writer(research_start_logs, delimiter=",", lineterminator="\r")
    file_writer.writerow(["Type", "Process", "Time_Start"])
    research_start_logs.close()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/start')
def start():
    type_research_start_logs = request.args.get('type')
    process_research_start_logs = request.args.get('process')
    with open('research_start_logs.csv', 'a', newline='') as research_start_logs:
        writer_object = writer(research_start_logs)
        writer_object.writerow([type_research_start_logs, process_research_start_logs, int(round(time.time() * 1000))])
        research_start_logs.close()

    name_file = type_research_start_logs + "_" + process_research_start_logs + ".csv"
    with open(name_file, mode="w", encoding='utf-8') as file:
        file_writer = writer(file, delimiter=",", lineterminator="\r")
        file_writer.writerow(["Time_Connect"])
        file.close()
    return 'File update'

@app.route('/run')
def run():
    return 'Run OK'

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
