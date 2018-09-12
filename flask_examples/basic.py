from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Dahmer"
    letters = list(name)
    pup_dictionary = {'pup_name':'Raditz'}
    #another exercise
    my_list = [1,2,3,4,5,6]
    kof_chars = ['iori', 'kyo','chang','mary']
    #bool
    user_log = True
    return render_template('basic.html',name=name,letters=letters,
                            pup_dictionary=pup_dictionary,my_list=my_list,
                            kof_chars=kof_chars,user_log=user_log)









if __name__ == '__main__':
    app.run(debug=True)
