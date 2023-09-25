from pico2d import *

running = True

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character_sonic = load_image('sonic.png')
# sprite size 805 x 483

def event_handle():
	global running

	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False

while running:
	frame = 0
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	# idle frame size 30, 50, pos 0, 433
	character_sonic.clip_draw(frame * 30, 433, 30, 50, TUK_WIDTH // 2, TUK_HEIGHT // 2, 50, 100)
	update_canvas()
	event_handle()
	delay(0.05)

close_canvas()
