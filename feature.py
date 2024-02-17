from  flask import Flask,render_template

FAI=Flask(__name__)
@FAI.route('/return_string')
def return_string():
    return 'this is kranthi'
@FAI.route('/return_html')
def return_html():
    return render_template('return_html.html')


if __name__=='__main__':
    FAI.run(debug=True)