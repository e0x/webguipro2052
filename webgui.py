from flask import Flask, request, url_for, redirect, abort, render_template, Response, make_response
#import serial
import myserial as serial
import time

ser = serial.Serial(
        port='/dev/null',
        baudrate=19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
)


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('control.html')


@app.route('/runcmd')
def runcmd():
	ser.open()
	ser.isOpen()
	Button = request.args.get('Button')
	ser.write(Button + '\r')
	time.sleep(1)
	ser.write('MA' + '\r')
	while ser.inWaiting() > 0:
		freq += ser.read(1)
	return 'freq' 


if __name__ == '__main__':
	app.debug = True
	app.run()
