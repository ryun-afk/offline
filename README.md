# offline
 Python 3.10.0


main.py:
    -initializes window, keyboard, debug
    -initializes target images for match template
    -filter window image and target images

    util folder:
        window.py
            -finds window
            -gets window size
            -refreshes computer vision
        
        keyboard.py 
            -record keyboard events
            -send keyboard events

        mouse.py*
            -get mouse position
            -control mouse

        debug
            -print fps
            -display computer vision
            -mark images with given locations

    process folder:
        targetimage.py
            -store: target image and dimensions
            -return image locations
            
        filter.py*
            -grayscale
            -blur


