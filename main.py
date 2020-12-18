import pygame


class Creature(pygame.sprite.Sprite):
    def __init__(self, pos, image, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -10)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, 10)
        if keys[pygame.K_d]:
            self.rect.move_ip(10, 0)
        if keys[pygame.K_a]:
            self.rect.move_ip(-10, 0)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    sprites = pygame.sprite.Group()
    creature = Creature((0, 0), pygame.image.load('data/creature.png'), sprites)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        sprites.update(pygame.key.get_pressed())
        screen.fill((255, 255, 255))
        sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
