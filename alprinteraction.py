import locale
locale.setlocale(locale.LC_ALL, 'C')

from openalpr import Alpr

def scanImage(imageFilePath):
    alpr = Alpr("gb", "/etc/openalpr/openalpr.conf", "/usr/local/src/openalpr/runtime_data")
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)

    alpr.set_top_n(20)
    alpr.set_default_region("md")

    results = alpr.recognize_file(imageFilePath)

    alpr.unload()

    if results and results['results'] and results['results'][0] and results['results'][0]['plate']:
        plate = results['results'][0]['plate']
        confidence = results['results'][0]['confidence']
        print("Suspected number plate: " + plate + " - " + str(confidence) + "%")

        return {"plate": plate, "confidence": confidence}
    
    return False
