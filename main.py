from flask import Flask, render_template
import psutil
app = Flask(__name__)

@app.route('/')
def sys_process():
    
    output = []
    for p in psutil.process_iter():
        try:

#             print(p.name(),p.status(),p.is_running(),p.username())
            pr_list = [p.name() , p.status() , p.is_running() , p.username()]
            print(pr_list)
            output.append(pr_list)
        except Exception as Error:
            print(Error)
        

    return render_template('index.html', processes=output)
#     print(output)
    
if __name__=='__main__': 
   app.run(debug=True) 