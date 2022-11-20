from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return f'This is a placeholder text for the Exercise 13.1. The correct path to check for prime numbers as per exercise instructions is at the <a href="/prime_number/">Prime Number</a> page'

@app.route('/prime_number/')
def prime():
    return f'Pass a number to the url after prime_number/ to do the tests.'

@app.route('/prime_number/<number>', methods=['GET'])
def prime_number(number):
    prime = True
    number = int(number)
    if number <= 1:
        return "Prime numbers must be greater than 1."
    else:
        for i in range(2, number):
            if (number % i) == 0:
                prime = False
                break
        if prime:
            return {"Number": number, "isPrime": prime}
        else:
            return {"Number": number, "isPrime": prime}

app.run(host='0.0.0.0', port=5000)