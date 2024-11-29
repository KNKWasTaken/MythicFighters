Akiro = {
    'move1': '''
message = 'Spectral Beam - DMG 2'
pygame.time.delay(1000)
{char}.newState('Spectral')
{atkframe}.newState('Spectral')
{char}.pendingState = 'Idle'
{atkframe}.pendingState = 'Default'
atk({victim}, 2)
''',
    'move2': '''
message = 'Stomp Smash - DMG 3'
pygame.time.delay(1000)
{char}.newState('Smash')
{atkframe}.newState('Smash')
{char}.pendingState = 'Idle'
{atkframe}.pendingState = 'Default'
atk({victim}, 3)
''',
    'move3': '''
if {char}.defence > 0:
    message = 'Shadow Veil - Defence Already Active'
    pygame.time.delay(1000)
else:
    message = 'Shadow Veil - DEF 2'
    pygame.time.delay(1000)
    {char}.newState('TransformShadow')
    {char}.pendingState = 'ShadowIdle'
    selfdef({char}, 2)
''',
    'move4': '''
if {char}.defence > 0:
    message = 'Soul Shield - Defence Already Active'
    pygame.time.delay(1000)
else:
    message = 'Soul Shield - DEF 3'
    pygame.time.delay(1000)
    {char}.newState('TransformSoul')
    {char}.pendingState = 'SoulIdle'
    selfdef({char}, 3)
'''
}

Mac = {
    'move1': '''
message = 'Fireball - DMG 2'
pygame.time.delay(1000)
{char}.newState('Ball')
{atkframe}.newState('Ball')
{char}.pendingState = 'Idle'
{atkframe}.pendingState = 'Default'
atk({victim}, 2)
''',
    'move2': '''
message = 'Firebeam - DMG 3'
pygame.time.delay(1000)
{char}.newState('Pillar')
{atkframe}.newState('Pillar')
{char}.pendingState = 'Idle'
{atkframe}.pendingState = 'Default'
atk({victim}, 3)
''',
    'move3': '''
if {char}.defence > 0:
    message = 'Firewall - Illegal Move'
    pygame.time.delay(1000)
else:
    message = 'Firewall - DEF 2'
    pygame.time.delay(1000)
    {char}.newState('TransformWall')
    {char}.pendingState = 'WallIdle'
    selfdef({char}, 2)
''',
    'move4': '''
if {char}.defence > 0:
    message = 'Firecoat = Illegal Move'
    pygame.time.delay(1000)
else:
    message = 'Firecoat - DEF 3'
    pygame.time.delay(1000)
    {char}.newState('TransformCoat')
    {char}.pendingState = 'CoatIdle'
    selfdef({char}, 3)
'''
}