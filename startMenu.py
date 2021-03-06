def start():
    import main
    from main import pygame, gui, width, height, buttonFont, mouse, titleFont, posText, spacebg
    
    green = (0, 255, 0)
    dark_green= (0, 200, 0)
    blue = (0, 0, 128)

    gui.fill((0, 0, 0))
    spacebg()
    startTitle = titleFont.render("Galactic Survival: Among You", True, green)
    setupButton = buttonFont.render("Setup Game", True, blue)
    instructions = buttonFont.render("Instructions", True, blue)

    #Allows events/actions from mouse/keyboard
    for event in pygame.event.get():
        #Close-Window 
        if event.type == pygame.QUIT:
           quit()
        #Mouse-Clicked commands
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40:
                main.screen = 1
            if width/2-60 <= mouse[0] <= width/2+60 and height/4*3 <= mouse[1] <= height/4*3+40:
                main.screen = 2

    #start rectangle
    if width/2-70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(gui, green,[width/2-70, height/2, 140, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_green, [width/2-70, height/2, 140, 40]) 

    #instructions rectangle
    if width/2-60 <= mouse[0] <= width/2+60 and height/4*3 <= mouse[1] <= height/4*3+40: 
        pygame.draw.rect(gui, green,[width/2-60, height/4*3, 120, 40]) 
        
    else: 
        pygame.draw.rect(gui, dark_green, [width/2-60, height/4*3, 120, 40]) 

    #title
    gui.blit(startTitle , posText(startTitle, width//2, 75))
    #start button 
    gui.blit(setupButton , (width/2-50, height/2+5))
    #instructions button
    gui.blit(instructions, (width/2-50, height/4*3+5))





