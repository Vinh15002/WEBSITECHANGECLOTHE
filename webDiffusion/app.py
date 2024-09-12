from flask import Flask, render_template,request
import os
app = Flask(__name__)

ficFlolder = os.path.join('static', 'displayData')

@app.route('/', methods = ['GET'])
def hello_world():
    
   
    imagelist = os.listdir('static/displayData')
    
    imagelist = ['displayData/' + image for image in imagelist]
    
    return render_template('b.html', imageList = imagelist)
    
@app.route('/', methods = ['POST'])
def predict_image():
    imagelist = os.listdir('static/displayData')
    imagelist = ['displayData/' + image for image in imagelist]
    # imagefile = request.files['imageperson']
    
    # image_path = 'images/' + imagefile.filename
    
    # imagefile.save(image_path)
    imageclothe = request.files.get('image2')
    return str(imageclothe)
    # imagclothe_path = 'images/test.jpg'
    # imageclothe.save(imagclothe_path)
    # return render_template('b.html', imageList = imagelist)
    
    
if __name__ == "__main__":
    app.run()