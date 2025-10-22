    import cv2

    # Load an image
    img = cv2.imread('your_image.jpg')

    # Get the dimensions of the image
    (h, w) = img.shape[:2]

    # Calculate the center of the image
    center = (w // 2, h // 2)

    # Define the rotation angle (e.g., 45 degrees) and scale
    angle = 45
    scale = 1.0

    # Get the rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, scale)

    # Rotate the image
    rotated_img = cv2.warpAffine(img, M, (w, h))

    # Display or save the rotated image
    cv2.imshow('Rotated Image', rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
