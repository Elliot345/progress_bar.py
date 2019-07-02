class bar:
  def progress_bar(num, end, use_display=False, display='new', exact=False):
    percent = round(num)
    if percent > 100:
      percent = 100
    if percent < 0:
      percent = 0
    if not use_display:
      if not end:
        print('[{}{}]'.format('█' * percent, ' ' * (100 - percent)), end='\r')
      else:
         print('[{}{}]'.format('█' * percent, ' ' * (100 - percent)))
    else:
      while True:
        try:
          import pygame
          pygame.init()
          pygame.font.init()
          break
        except:
          import os
          os.system('pip3 install pygame')
      if display == 'new':
        display = pygame.display.set_mode((600, 200))
        auto_x = 0
        auto_y = 0
      else:
        w, h = pygame.display.get_surface().get_size()
        auto_x = (w / 2) - (600 / 2)
        auto_y = (h - 200)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
      def draw_thing(x, y, size, text):
        myfont = pygame.font.SysFont('arialhebrewdeskinterface', size)
        textsurface = myfont.render('{}'.format(text), False, (0, 0, 0))
        width = textsurface.get_width()
        display.blit(textsurface, (x - (width / 2), y))
      display.fill((0, 0, 255))
      
      pygame.draw.line(display, (0, 0, 0), [auto_x + 30, auto_y + 30], [(600 - 30) + auto_x, auto_y + 30])
      pygame.draw.line(display, (0, 0, 0), [(600 - 30) + auto_x, 30 + auto_y], [(600 - 30) + auto_x, (200 - 30) + auto_y])
      pygame.draw.line(display, (0, 0, 0), [(600 - 30) + auto_x, (200 - 30) + auto_y], [auto_x + 30, (200 - 30) + auto_y])
      pygame.draw.line(display, (0, 0, 0), [30 + auto_x, (200 - 30) + auto_y], [30 + auto_x, 30 + auto_y])
      
      pygame.draw.rect(display, (0, 255, 0), (31 + auto_x, 31 + auto_y, ((600 - 60) * (0.01 * num)) - 2, (200 - 60) - 1))
      if not exact:
        draw_thing(300 + auto_x, 0 + auto_y, 35, '{}%'.format(percent))
      else:
        draw_thing(300 + auto_x, 0 + auto_y, 35, '{}%'.format(num))
      for i in range(11):
        pygame.draw.line(display, (0, 0, 0), [(((600 - 60) * (0.1 * i)) + 30) + auto_x, 30 + auto_y], [(((600 - 60) * (0.1 * i)) + 30) + auto_x, (200 - 30) + auto_y])
        draw_thing((((600 - 60) * (0.1 * i)) + 30) + auto_x, (200 - 30) + auto_y, 25, i * 10)
      pygame.display.update()
#'█' = chr(9608)
