import states_daily_parser as sdp
import state_district_wise_parser as sdwp
import model as m
dataset = m.initialize()

def check_confirmed():

        for states in dataset[:-1]:
                
                if sdp.total_count(states['code']) == sdwp.total_count(states['code']):

                        print(states['name'], '   all is well')
                else:
                        print('all is not well in ', states['name'])

def controller():
    
    print('Press 1 to get cumulative data.')
    print('press 2 to get cumulative series datewise data.')
    print('Press 3 to get cumulative data of last 3 days.')
    print('Press 4 to get cumulative data of last 3 days for all states.')
    print('Press 5 to quit')

    choice = 0

    while choice != 3:

        choice = int(input('enter your choice: '))

        if choice == 1:

            date_to_fetch = input('Enter date:')
            state_code = input('Enter state code:')

            sdp.cumulative_data(date_to_fetch, state_code)
        elif choice == 2:

            date_to_fetch = input('Enter date:')
            state_code = input('Enter state code:')

            sdp.cumulative_series_datewise_data(date_to_fetch, state_code)
        elif choice == 3:

            state_code = input('Enter state code:')

            sdp.cumulative_last_3_days(state_code)
        
        elif choice == 4:

            sdp.cumulative_last_3_days_all_states()
            
        elif choice == 5:
            break
        else:
            print('Invalid choice, please choose again\n')

    print("\nProgram has quit")
        
#controller()
check_confirmed()
