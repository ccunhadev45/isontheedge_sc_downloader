import soundcloud, requests, os, re, sys
import socket, json

from tqdm import tqdm
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4, MP4Cover
from mutagen.flac import FLAC
from mutagen.id3 import ID3, TIT2, TPE1, TCON, TDRC, APIC
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from halo import Halo

# Function to check if a directory exists
def dir_exists(path):
    return os.path.isdir(path)

# Function to create a directory if it doesn't exist
def create_dir(path):
    if not dir_exists(path):
        os.makedirs(path)

# Function to download a file
def download_file(url, filename, chunk_size=1024):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as f:
        for chunk in tqdm(response.iter_content(chunk_size=chunk_size), total=response.headers.get('Content-Length', 1)):
            f.write(chunk)

# Function to tag a file (MP3, MP4, FLAC) with metadata
def tag_file(filename, title, artist, genre, album, year, track_number, comment, artwork_url=None):
    file_type = filename.split('.')[-1].lower()

    if file_type == 'mp3':
        tag = MP3(filename)
    elif file_type == 'm4a':
        tag = MP4(filename)
    elif file_type == 'flac':
        tag = FLAC(filename)
    else:
        return

    tag['title'] = TIT2(title)
    tag['artist'] = TPE1(artist)
    tag['genre'] = TCON(genre)
    tag['album'] = TALB(album)
    tag['year'] = TDRC(year)
    tag['tracknum'] = TRCK(track_number)
    tag['comment'] = COMM(comment)

    if artwork_url:
        response = requests.get(artwork_url, stream=True)
        response.raise_for_status()
        artwork_data = response.content
        tag['APIC'] = APIC(3, 'jpg', artwork_data)

    tag.save()

# Function to validate a filename to ensure it's safe for saving
def validate_name(filename):
    invalid_chars = re.compile('[\\/:*?"<>|]')
    return re.sub(invalid_chars, '_', filename)

# Function to generate a filename based on track information
def get_filename(track, extension='mp3'):
    title = validate_name(track['title'])
    artist = validate_name(track['user']['username'])

    filename = f'{artist} - {title}.{extension}'

    return filename

# Function to check internet connectivity
def is_connected():
    try:
        socket.gethostbyname('google.com')
        return True
    except socket.gaierror:
        return False

# Function to generate a random string
def generate_random_string(length=10):
    import string
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])

# Function to retry requests in case of network errors
def retry_requests(retries=3, backoff_factor=2):
    session = requests.Session()
    retry = Retry(total=retries, backoff_factor=backoff_factor)
    adapter = HTTPAdapter(max_retries=retry)
    session.adapters['http'] = adapter
    return session

# Function to create a spinner using Halo
def create_spinner(text, spinner_type='dots'):
    spinner = Halo(text=text, spinner_type=spinner_type, color='cyan')
    return spinner
