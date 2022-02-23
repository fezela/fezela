

SETTINGS = {

'windows_managers': ['NCURSES'],
'selected_win_manager': 'NCURSES'

        }

GAMESTATE = {

    'COMBAT': {
        'in_Combat': False,
        'AMBUSH': {
            'determined': False,
            'ambushed': False,
            },
        'determined_Initiative': False,
        'assigned_Counter': False,
        'determined_Actions': False,
        'updated': False, #Possibly not necessary
        'taken_Turn': False #Possibly not necessary
            },
    'INVENTORY': {    
        'in_Inventory': False,
        'in_Menu': False,
        'in_Exploration': False,
    },
    'started': False
        }

