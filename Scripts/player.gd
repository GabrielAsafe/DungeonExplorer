extends CharacterBody2D

var speed = 400  # speed in pixels/sec
@export var aceleretion = 0
var prevAnim = "1"
var running = false
var playing = false
var current_animation = ""


enum State {
	IDLE,
	WALK,
	RUN,
	ATTACK,
	INTERACT,
	ROLL,
	DEFEND,
	CAST
}

var state = State.IDLE

func _ready():
	get_node("AnimationPlayer").animation_finished.connect(_on_AnimationPlayer_animation_finished)
	print("Signal connected")  # Instrução de depuração

func controls(delta):
	var input_dir = Input.get_vector("left", "right", "up", "down")
	if input_dir.length() != 0 and !playing:
		var a = input_dir.angle() / (PI/4)
		a = wrapi(int(a), 0, 8)
		prevAnim = a
		if Input.is_action_pressed("run"):
			state = State.RUN
			aceleretion = 50
		else:
			state = State.WALK
			aceleretion = 10
	elif input_dir.length() == 0 and !playing:
		state = State.IDLE
		aceleretion = 0

	velocity = input_dir * speed * delta * aceleretion
	move_and_slide()

	if !playing:
		match state:
			State.IDLE:
				current_animation = "idle" + str(prevAnim)
			State.WALK:
				current_animation = "walk" + str(prevAnim)
			State.RUN:
				current_animation = "run" + str(prevAnim)
		
		$AnimationPlayer.play(current_animation)

func _physics_process(delta):
	controls(delta)

func _input(_event):
	if Input.is_action_just_pressed("attack") and !playing:
		state = State.ATTACK
		play_action("atk")
	elif Input.is_action_just_pressed("interact") and !playing:
		state = State.INTERACT
		play_action("interact")
	elif Input.is_action_just_pressed("roll") and !playing:
		state = State.ROLL
		play_action("roll")
	elif Input.is_action_just_pressed("defend") and !playing:
		state = State.DEFEND
		play_action("defend")
	elif Input.is_action_just_pressed("cast") and !playing:
		state = State.CAST
		play_action("cast")

func play_action(action):
	playing = true
	current_animation = action + str(prevAnim)
	$AnimationPlayer.play(current_animation)


func _on_AnimationPlayer_animation_finished(anim_name):
	if anim_name.begins_with("atk") or anim_name.begins_with("interact") or anim_name.begins_with("roll") or anim_name.begins_with("defend") or anim_name.begins_with("cast"):
		playing = false  # Marca a animação como não mais em execução
		state = State.IDLE



