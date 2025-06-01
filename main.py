import pygame
pygame.init()
size = 1
color = (0, 0, 0)
screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))
pygame.display.update()

while True:
    line = input()
    qtype = line.split()[0]

    if qtype == "end":
        pygame.image.save(screen, 'draw.png')
        break
    elif qtype == "change":
        if line.split()[1] == "size":
            size = int(line.split()[2])
        else:
            color = int(line.split()[2]), int(line.split()[3]), int(line.split()[4])
    else:
        shape = line.split()[1]
        if shape == "line":
            pygame.draw.line(screen, color, (int(line.split()[2]), int(line.split()[3])),
                             (int(line.split()[4]), int(line.split()[5])), size)
        elif shape == "circle":
            pygame.draw.circle(screen, color, (int(line.split()[2]), int(line.split()[3])), int(line.split()[4]), size)
        else:
            points = []
            for i in range(2, len(line.split()), 2):
                points.append((int(line.split()[i]), int(line.split()[i + 1])))
            pygame.draw.polygon(screen, color, points, size)
    pygame.display.update()
    pygame.event.pump()