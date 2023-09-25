from pico2d import *

running = True

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character_sonic = load_image('sonic.png')
# sprite size 805 x 483
# y size default 49
# 4, 5th y size 70 : 49 * 7 + 70 * 2 = 483

def event_handle():
	global running

	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False

frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
sonic_size = 60, 100

while running:
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

	# draw idle animation
	# idle animation frame size: 30, 49, start pos: 0, 434(483 - 49)
	# character_sonic.clip_draw(frame * 30, 434, 30, 49, x, y, *sonic_size)

	# draw running animation
	# running animation frame size: 37, 49, start pos: 0, 385(434 - 39)
	character_sonic.clip_draw(frame * 37, 385, 37, 49, x, y, *sonic_size)

	update_canvas()
	event_handle()

	frame = (frame + 1) % 6

	delay(0.05)

close_canvas()
