import states_daily_parser as sdp
import state_district_wise_parser as sdwp
import model as m
dataset = m.initialize()

def check_confirmed():

        for states in dataset[:-1]:
                
                result = sdp.total_count(states['code'])
                if result['Confirmed'] == sdwp.total_count(states['code']):

                        print(states['name'], '   all is well')
                else:
                        print('all is not well in ', states['name'])

def controller():
    
    print('Press 1 to get cumulative data.')
    print('press 2 to get cumulative series datewise data.')
    print('Press 3 to get cumulative data of last 3 days.')
    print('Press 4 to get cumulative data of last 3 days for all states.')
    print('Press 5 to get data frame of total confirmed,recovered and deceased data till latest date')
    print('Press 6 to get data frame of statewise cumulative last 3 days confirmed data')
    print('Press 7 to get data frame of statewise cumulative last 3 days recovered data')
    print('Press 8 to get data frame of statewise cumulative last 3 days deceased data')
    print('Press 9 to get data frame of statewise confirmed data from start date to current date as in JSON file')
    print('Press 10 to get data frame of statewise recovered data from start date to current date as in JSON file')
    print('Press 11 to get data frame of statewise deceased data from start date to current date as in JSON file')
    print('Press 12 to get data frame of cumulative statewise confirmed data from start date to current date')
    print('Press 13 to get data frame of cumulative statewise recovered data from start date to current date')
    print('Press 14 to get data frame of cumulative statewise deceased data from start date to current date')
    print('Press 15 to know whether date in states_daily_json and data in state_district_wise.json are same or not.')
    print('Press 16 to quit')


    choice = 0

    while choice != 16:

        choice = int(input('enter your choice: '))

        if choice == 1:

            date_to_fetch = input('Enter date:')
            state_code = input('Enter state code:')
            if state_code.islower() == False:
                state_code = state_code.lower()
            else:
                state_code = state_code

            if sdp.state_code_validate(state_code) != 0:

                if sdp.date_validate(date_to_fetch) != 0:

                    if sdp.cumulative_data(date_to_fetch, state_code) == 0:
                        print('Date does not exist')
                    else:
                        print(sdp.cumulative_data(date_to_fetch, state_code))
                else:
                    
                    continue
            else:
                if sdp.date_validate(date_to_fetch) == 0:
                    continue
                else: 
                    continue
            
        elif choice == 2:

            date_to_fetch = input('Enter date:')
            state_code = input('Enter state code:')
            if state_code.islower() == False:
                state_code = state_code.lower()
            else:
                state_code = state_code

            if sdp.state_code_validate(state_code) != 0: 
                if sdp.date_validate(date_to_fetch) != 0:
                    returned_dict = sdp.cumulative_series_datewise_data(date_to_fetch, state_code)
                    for date in returned_dict:
                        print(date, returned_dict[date])
                else:
                    continue
            else:
                if sdp.date_validate(date_to_fetch) == 0:
                    continue
                else: 
                    continue

        elif choice == 3:

            state_code = input('Enter state code:')
            if state_code.islower() == False:
                state_code = state_code.lower()
            else:
                state_code = state_code

            if sdp.state_code_validate(state_code) != 0: 
                returned_dict = sdp.cumulative_last_3_days(state_code)
                for date in returned_dict:
                        print(date, returned_dict[date])
            else:
                continue
        
        elif choice == 4:  

            returned_dict = sdp.cumulative_last_3_days_all_states(choice)
            for state in returned_dict:
                    print(state)
                    for date in returned_dict[state]:
                        print(date, returned_dict[state][date])

        elif choice == 5:

            print(sdp.make_data_frame())

        elif choice == 6:

            print(sdp.cumulative_last_3_days_confirmed_dataframe(choice))

        elif choice == 7:

            print(sdp.cumulative_last_3_days_recovered_dataframe(choice))

        elif choice == 8:

            print(sdp.cumulative_last_3_days_deceased_dataframe(choice))

        elif choice == 9:

            print(sdp.all_data_confirmed())

        elif choice == 10:

            print(sdp.all_data_recovered())

        elif choice == 11:

            print(sdp.all_data_deceased())

        elif choice == 12:

            print(sdp.cumulative_all_data_confirmed())

        elif choice == 13:

            print(sdp.cumulative_all_data_recovered())

        elif choice == 14:

            print(sdp.cumulative_all_data_deceased())
 
        elif choice == 15:

            check_confirmed()
            
        elif choice == 16:
            break

        else:
            print('Invalid choice, please choose again\n')

    print("\nProgram has quit")
        
controller()
