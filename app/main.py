from flask import blueprints
from flask import Flask, render_template, request
from predict_meme import predict_meme
from flask.helpers import send_from_directory
import os
app = Flask(__name__)

# @app.route('/download/', methods=['POST'])
# def user_download():
#     url = request.args['img']  # user provides url in query string
#     r = request.get(url)

#     # write to a file in the app's instance folder
#     # come up with a better file name
#     with app.open_instance_resource('downloaded_file', 'wb') as f:
#         f.write(r.content)

@app.route('/', methods = ['POST', 'GET'])
def index():

  if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.root_path, "./static/" + f.filename))
      
      return render_template('home_page.html', f = f.filename, )
  return render_template('home_page.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
  a=(request.args.get('fname'))
  f=(request.args.get('img'))
  a = predict_meme(a)
  return  render_template('home_page.html',f=f,a=a)


    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 
