"""
You’re going to draw a face with eyes that will follow the mouse!
"""

# 1. Find an image on the internet and drop it into your sketch.
# It can be anything as long as it has large eyes!

def setup():
    # 2. Import your image using the following code:
    # global face
    # face = loadImage("big_eye_bird.png")
    global frog
    frog = loadImage("FROG.jpg")

    
    # 3. Set the size of your sketch and the size of your image to be
    # the same by entering the following code in the setup method.
    # size(800, 600)
    # face.resize(width, height)
    size(800, 600)
    frog.resize(width, height)

    
def draw():
    # 4. Draw your image using:
    # global face
    # background(face)
    global frog
    background(frog)

    # 5. Place a white ellipse over the left eye of your image.
    # fill(<your color>)
    # ellipse(x, y, width, height)
    fill(255, 50, 20)
    ellipse(655, 195, 130, 240)
    
    println(str(mouseX) + ' ' + str(mouseY))   
    
    # 6. Now add a pupil (the black part) to the left eye earlier.
    # Use the pupil x and y variables for the position.
    fill(0, 0, 0)
    ellipse(655, 195, 16, 16)
    
    # 7. Run the program and check if the left eye is in the correct
    # position
    
    # 8. To make the pupil follow the mouse, the pupil's x and y positions
    # should be set to mouseX and mouseY when the mouse is inside the eye.
    # Use the is_mouse_inside_eye() function for this.
    #
    # If the mouse is not inside the eye, call the get_eye_position()
    # function:
    # position = get_eye_position(left_eye_x, left_eye_y, eye_radius, pupil_radius)
    # ellipse(position.x, position.y, pupil_radius * 2, pupil_radius * 2)
    if is_mouse_inside_eye_ellipse(655, 195, 65, 120, 8):
        fill(255, 50, 20)
        ellipse(655, 195, 130, 240)
        fill(0, 0, 0)
        ellipse(mouseX, mouseY, 16, 16)
    
    # 9. Repeat the steps above for the right eye and observe the googly eyes!

# ======================= DO NOT MODIFY THE CODE BELOW ==========================

def is_mouse_inside_eye(eye_center_x, eye_center_y, eye_radius, pupil_radius):
    dist_x = mouseX - eye_center_x;
    dist_y = mouseY - eye_center_y;
    distance = sqrt( (dist_x * dist_x) + (dist_y * dist_y) )
    
    if distance <= eye_radius - pupil_radius:
        return True
    
    return False

def is_mouse_inside_eye_ellipse(eye_center_x, eye_center_y, eye_radius_x, eye_radius_y, pupil_radius):
    dist_x = mouseX - eye_center_x;
    dist_y = mouseY - eye_center_y;
    if dist_x<0:
        dist_x -= pupil_radius
    else:
        dist_x += pupil_radius
    if dist_y<0:
        dist_y -= pupil_radius
    else:
        dist_y += pupil_radius
    equation = (dist_x*dist_x)/(eye_radius_x*eye_radius_x) + (dist_y*dist_y)/(eye_radius_y*eye_radius_y)
    
    if equation <= 0.9:
        return True
    
    return False


def get_eye_position(eye_center_x, eye_center_y, eye_radius, pupil_radius):
    position = Position()
    
    if mouseX - eye_center_x != 0:
        angle = atan2( mouseY - eye_center_y, mouseX - eye_center_x )
        position.x = eye_center_x + ((eye_radius - pupil_radius) * cos(angle))
        position.y = eye_center_y + ((eye_radius - pupil_radius) * sin(angle))

    return position

class Position:
    x = float()
    y = float()
