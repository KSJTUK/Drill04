from pico2d import *

running = True

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character_sonic = load_image('sonic.png')
# sprite size 805 x 483

def event_handle():
	pass

while running:
	frame = 0
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
	# idle frame size 30, 50, pos 0, 433
	character_sonic.clip_draw(frame * 30, 433, 30, 50, TUK_WIDTH // 2, TUK_HEIGHT // 2, 50, 100)
	update_canvas()
	delay(1)
	break

close_canvas()
