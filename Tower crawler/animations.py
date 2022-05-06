import random
from kivy.core.image import Image
from kivy.atlas import Atlas
sprites = {
	'player':None,
	'misc':None,
	'enemy':None}
	
anim = {
	'stay blink':None,
	'mage blink':None,
	'fade':None,
	'move':None,
	'sword blink':None,
	'armor blink':None,
	'potion blink':None,
	'gold blink':None}

def uploading_sprites():
	a = {'player':Atlas('/storage/emulated/0/kivy/Tower Crawler/resources/sprites/player.atlas'),'misc':Atlas('/storage/emulated/0/kivy/Tower Crawler/resources/sprites/misc.atlas'),'enemy':Atlas('/storage/emulated/0/kivy/Tower Crawler/resources/sprites/enemy.atlas')}
	for t in a['player'].original_textures:
		t.mag_filter = 'nearest'
	for t in a['enemy'].original_textures:
		t.mag_filter = 'nearest'
	for t in a['misc'].original_textures:
		t.mag_filter = 'nearest'
	sprites['player'] = {
		'player':a['player']['player'],
		'player jump':a['player']['player jump'],
		'armored':a['player']['armored'],
		'armored jump':a['player']['armored jump'],
		'broken':a['player']['broken'],
		'dead':a['player']['dead'],
		'invul':a['player']['invul'],
		'invul armored':a['player']['invul armored'],
		'invul jump':a['player']['invul jump'],
		'invul armored jump':a['player']['invul armored jump'],
		'ability':a['player']['ability'],
		'ability armored':a['player']['ability armored']}

	sprites['misc'] = {
		'pad':a['misc']['pad'],
		'broken':a['misc']['broken'],
		'thorns':a['misc']['thorns'],
		'null':a['misc']['null'],
		'armor':a['misc']['armor'],
		'armor1':a['misc']['armor1'],
		'armor2':a['misc']['armor2'],
		'potion':a['misc']['potion'],
		'potion1':a['misc']['potion1'],
		'potion2':a['misc']['potion2'],
		'sword':a['misc']['sword'],
		'sword1':a['misc']['sword1'],
		'sword2':a['misc']['sword2'],
		'gold':a['misc']['gold'],
		'gold1':a['misc']['gold1'],
		'gold2':a['misc']['gold2']}

	sprites['enemy'] = {
		'move':a['enemy']['move'],
		'move dead':a['enemy']['move dead'],
		'move1':a['enemy']['move1'],
		'move2':a['enemy']['move2'],
		'stay':a['enemy']['stay'],
		'stay dead':a['enemy']['stay dead'],
		'stay blink':a['enemy']['stay blink'],
		'mage':a['enemy']['mage'],
		'mage dead':a['enemy']['mage dead'],
		'mage blink':a['enemy']['mage blink'],
		'fade0':a['enemy']['fade0'],
		'fade1':a['enemy']['fade1'],
		'fade2':a['enemy']['fade2'],
		'fade3':a['enemy']['fade3'],
		'portal':a['enemy']['portal'],}
	
	anim['stay blink']=(
	(sprites['enemy'])['stay blink'],
	(sprites['enemy'])['stay'])
	
	anim['fade'] = (
	(sprites['enemy'])['fade0'],
	(sprites['enemy'])['fade1'],
	(sprites['enemy'])['fade2'],
	(sprites['enemy'])['fade3'],
	(sprites['misc'])['null'],
	(sprites['misc'])['null'],
	(sprites['misc'])['null'],
	(sprites['misc'])['null'],
	(sprites['misc'])['null'],
	(sprites['misc'])['null'],
	(sprites['misc'])['null'],
	(sprites['enemy'])['fade3'],
	(sprites['enemy'])['fade2'],
	(sprites['enemy'])['fade1'],
	(sprites['enemy'])['fade0'],
	(sprites['enemy'])['mage'])
	
	anim['move']=(
	(sprites['enemy'])['move'],
	(sprites['enemy'])['move1'],
	(sprites['enemy'])['move2'],
	(sprites['enemy'])['move1'])
	
	anim['mage blink']=(
	(sprites['enemy'])['mage blink'],
	(sprites['enemy'])['mage'])
	
	anim['sword blink']=(
	(sprites['misc'])['sword1'],
	(sprites['misc'])['sword2'],
	(sprites['misc'])['sword1'],
	(sprites['misc'])['sword'])
	
	anim['potion blink']=(
	(sprites['misc'])['potion1'],
	(sprites['misc'])['potion2'],
	(sprites['misc'])['potion1'],
	(sprites['misc'])['potion'])
	
	anim['armor blink']=(
	(sprites['misc'])['armor1'],
	(sprites['misc'])['armor2'],
	(sprites['misc'])['armor1'],
	(sprites['misc'])['armor'])
	
	anim['gold blink']=(
	(sprites['misc'])['gold1'],
	(sprites['misc'])['gold2'],
	(sprites['misc'])['gold1'],
	(sprites['misc'])['gold'])
	
def animate(name,time):
	if not name == '':
		return(anim[name])[time]

