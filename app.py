from flask import Flask, render_template, request, jsonify, url_for
import os

app = Flask(__name__)

# Your existing routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video/<int:video_id>')
def video_details(video_id):
    # Your existing code for video details
    pass

# New route for handling video upload
@app.route('/upload', methods=['POST'])
def upload_video():
    try:
        video_file = request.files['video']
        
        # Save the video file to a directory (customize the directory as needed)
        upload_folder = 'static/uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        video_path = os.path.join(upload_folder, 'uploaded_video.mp4')
        video_file.save(video_path)

        # Provide the URL of the uploaded video
        video_url = url_for('static', filename=f'uploads/uploaded_video.mp4')

        return jsonify({'success': True, 'video_url': video_url})
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'success': False})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

