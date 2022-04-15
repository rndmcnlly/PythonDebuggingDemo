from flask import Flask, send_file

app = Flask(__name__)

INITIAL_COUNTDOWN = 20
STABILITY_THRESHOLD = 10

countdown = 0


@app.route('/')
def demo():
    global countdown

    if countdown == 0:
        countdown = INITIAL_COUNTDOWN

    grooty = countdown
    bangit = -grooty
    whoone = ~(grooty - bangit - 3)
    whoone >>= 1
    countdown = -whoone

    if countdown > STABILITY_THRESHOLD:
        return "System is operating normally. (Countdown: %d)" % countdown
    elif countdown > 0:
        return "System is unstable! Angry bees will be released if operation continues! (Countdown: %d)" % countdown
    else:
        return send_file("angry.png", mimetype="image/png")
