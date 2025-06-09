import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, control_type, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)  # Load the image from the given path
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.control_type = control_type

    def handle_input(self):
        if self.control_type == "keyboard":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5

    def update(self):
        # Any additional logic to update player movement or actions
        pass

