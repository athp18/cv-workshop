from matplotlib.pyplot import plt
# Function to add an image to a subplot with proper scaling
def add_subplot(position, img, title):
    ax = plt.subplot(1, 4, position)
    
    # Get the aspect ratio of the image
    img_height, img_width = img.shape[:2]
    aspect_ratio = img_width / img_height
    
    # Set the limits of the plot to match the subplot box
    ax.set_xlim(-width/2, width/2)
    ax.set_ylim(-height/2, height/2)
    
    # Calculate the display dimensions to maintain aspect ratio
    if img_width != width or img_height != height:
        display_height = height
        display_width = height * aspect_ratio
        if display_width > width:
            display_width = width
            display_height = width / aspect_ratio
            
        # Center the image in the subplot
        x_offset = (width - display_width) / 2
        y_offset = (height - display_height) / 2
        
        extent = [
            -width/2 + x_offset, 
            -width/2 + x_offset + display_width,
            -height/2 + y_offset,
            -height/2 + y_offset + display_height
        ]
    else:
        extent = [-width/2, width/2, -height/2, height/2]
    
    # Display the image
    ax.imshow(img, extent=extent)
    
    # Add a border to show the subplot boundaries
    ax.set_box_aspect(1)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
