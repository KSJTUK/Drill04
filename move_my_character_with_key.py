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
	global running, dirX, dirY, animation

	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			animation = "running"
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_LEFT:
				dirX -= 1
			elif event.key == SDLK_RIGHT:
				dirX += 1
			elif event.key == SDLK_UP:
				dirY += 1
			elif event.key == SDLK_DOWN:
				dirY -= 1
		elif event.type == SDL_KEYUP:
			animation = "idle"
			if event.key == SDLK_LEFT:
				dirX += 1
			elif event.key == SDLK_RIGHT:
				dirX -= 1
			elif event.key == SDLK_UP:
				dirY -= 1
			elif event.key == SDLK_DOWN:
				dirY += 1

dirX, dirY = 0, 0
frame_y = 434
frame_size = 30, 49
frame_cnt = 6
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
sonic_size = 60, 100
animation = "idle"

# set sonic's animation
def set_sonic_animation(animation):
	global frame_size, frame_cnt, frame_y

	if animation == "idle":
		frame_size = 30, 49
		frame_cnt = 6
		frame_y = 434
	elif animation == "running":
		frame_size = 37, 49
		frame_cnt = 9
		frame_y = 385

while running:
	tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

	# draw idle animation
	# idle animation frame size: 30, 49, start pos: 0, 434(483 - 49)
	# character_sonic.clip_draw(frame * 30, 434, 30, 49, x, y, *sonic_size)

	# draw running animation
	# running animation frame size: 37, 49, start pos: 0, 385(434 - 39)
	# character_sonic.clip_draw(frame * 37, 385, 37, 49, x, y, *sonic_size)

	character_sonic.clip_draw(frame * frame_size[0], frame_y, *frame_size, x, y, *sonic_size)

	update_canvas()
	event_handle()

	set_sonic_animation(animation)

	frame = (frame + 1) % frame_cnt
	x += dirX * 5
	y += dirY * 5

	delay(0.05)

close_canvas()
