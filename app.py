import time
from flask import Flask, request, render_template, Response, json

app = Flask(__name__)


messageList = [{'name' : 'Rohit', 'message' : "Hello Students :hiii"}]


@app.route('/send-broadcast/<name>/<msg>', methods=['POST'])
def webhook(name, msg):
    messageList.append({'name': name, 'message': msg})
    print(messageList)
    return {'message' : 'added success'}, 200


@app.route('/send-broadcast')
def watch():
    return render_template('watch.html', messages=messageList)

@app.route('/stream')
def stream():
    prevLen = 0
    def response():
        nonlocal prevLen
        
        currLen = len(messageList)
        if (currLen != prevLen):
            prevLen = currLen
            yield f"data: {messageList[-1]['name']} : {messageList[-1]['message']}\n\n"
        time.sleep(1)
    return Response(response(), mimetype='text/event-stream')


@app.route('/send-broadcast')
def send():
    return render_template("send.html")



    








if __name__ == "__main__":
    app.run(debug=True)