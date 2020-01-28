import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Which city would you like to explore: \n')
    print('*****************************')
    print('*        chicago            *')
    print('*     new york city         *')
    print('*       washington          *')
    print('*****************************')
    while True:
	    city = input('Enter choiced city: ').lower()
	    if city not in ('chicago', 'new york city', 'washington'):
		    print("sorry!!!!! Invalid input")
		    continue
	    else:
		    break
   # TO DO: get user input for month (all, january, february, ... , june)
    print('Which month would you like to explore:')
    print('*****************************')
    print('*        all                *')
    print('*      january              *')
    print('*      february             *')
    print('*       march               *')
    print('*       april               *')
    print('*        may                *')
    print('*       june                *')
    print('*****************************')
    while True:
        month = input('Enter choiced month: ').lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("sorry!!!!! Invalid input")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day would you like to explore:')
    print('*****************************')
    print('*          all              *')
    print('*        monday             *')
    print('*        tuesday            *')
    print('*       wednesday           *')
    print('*       thursday            *')
    print('*        friday             *')
    print('*       saturday            *')
    print('*        sunday             *')
    print('*****************************')
    while True:
        day = input('Enter choiced day: ').lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("sorry!!!!! Please enter right day:")
            continue
        else:
            break
    print()
    print('YOU HAVE CHOSEN THE INFO BELOW TO ANALYSE:')
    print('City: ', city.lower())
    print('Month: ', month.lower())
    print('Day: ', day.lower())

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_week_day = df['day_of_week'].mode()[0]
    print('most_common_week_day:', most_common_week_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('most_common_start_hour', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station:',start_station)
    print('most commonly used start station:',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('most commonly used end station: ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start and end station is/are :', start_station, "and", end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('total travel time: ', total_travel_time/86400, "days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time: ', mean_travel_time/60, "munites")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of user type:\n',user_types)

    # TO DO: Display counts of gender
    try:
	    gender_count = df['Gender'].value_counts()
	    print('Gender type:\n',gender_count)
	    print()
    except:
	    print('sorry, gender info not found for this city.')
	    print()

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
	    earliest_year_of_birth = df['Birth Year'].min()
	    most_common_year_of_birth = df['Birth Year'].mode()
	    most_recent_year_of_birth = df['Birth Year'].max()

	    print('INFO FOR BIRTH YEAR')
	    print('Earliest year of birth: ',int(earliest_year_of_birth))
	    print('most common year of birth: ', int(most_common_year_of_birth))
	    print('most recent year of birth: ', int(most_recent_year_of_birth))

    except:
	    print('sorry, Year info not found for this city')
	    print('so, no info about Earliest year of birth,most common year of birth,most recent year of birth. ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




    #create a function to view raw data
def raw_data(df):
    response = input('\nWould you like to raw data? Enter yes or no: \n')
    st=0
    while True:
        if response.lower()!='no':
            more = df.iloc[st: st+5]
            print(more)
            st +=5
            response = input('\nWould you like to see more data? Enter yes or no: \n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
