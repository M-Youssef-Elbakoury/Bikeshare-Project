import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june' ]
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city would you like to display its data? (chicago, new york, washington): ').lower()
        if city not in CITY_DATA:
            print('Please inter a valid city name.')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month?: (january, february, march, april, may, june) or type all to display all months: ').lower()
        if month not in months:
            print('Please inter a valid month name.')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day?: (sudnay, monday, tuesday, wednesday, thursday, friday, saturday) or type all to display all days: ').lower()
        if day not in days:
            print('Please inter a valid day name.')
        else:
            break
            
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['Month'] == month.title()]
    
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df



def user_inputs_message(city, month, day):
    """Displays message to show the inputs of the users."""
    print('-'*70)
    print('\nAll upcoming process will be implemented on the data of {} city, {} month/s, {} day/s.\n'.format(city, month, day))
    print('-'*70)
    
    
    
def display_5_raws(df):
    """
    The function display 5 rows of the data every time upon request by the user
    """
    row = 0
    rows_display = input('Would you like to display the first 5 rows of the data? Yes or No: ').lower()
    while True:
        if rows_display == 'no':
            break
        if rows_display == 'yes':
            print(df.iloc[row:row+5])
            rows_display = input('would you like to display the next 5 rows of the data? Yes or No: ').lower()
            row += 5
        else:
            rows_display = input('Invalid input\nWould you like to display 5 rows of the data? Yes or No: ').lower()
            print(rows_display)
    
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('-'*70)
    print('\n')
    print('-'*40)
    print('Calculating The Most Frequent Times of Travel.')
    print('-'*40)
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print('The most common month is {}.'.format(common_month))

    # display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print('The most common day is {}.'.format(common_day))

    # display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print('The most common hour is {}.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*70)
    print('\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('-'*40)
    print('Calculating The Most Popular Stations and Trip...')
    print('-'*40)
    start_time = time.time()

    # display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}.'.format(commonly_used_start_station))

    # display most commonly used end station
    commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}.'.format(commonly_used_end_station))

    # display most frequent combination of start station and end station trip
    commonly_used_start_and_end_station = (df['Start Station']+" --- "+df['End Station']).mode()[0]
    print('The most commonly used combination of start and end station: {}.'.format(commonly_used_start_and_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
    print('\n')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('-'*40)
    print('Calculating Trip Duration...')
    print('-'*40)
    start_time = time.time()

    # display total travel time
    total_traval_time = df['Trip Duration'].sum()
    print('Total travel time; \nIn seconds: {} seconds. \nIn minutes: {} minutes. \nIn hours: {} hours.'.format(total_traval_time, total_traval_time//60, total_traval_time//3600))

    # display mean travel time
    mean_traval_time = int(df['Trip Duration'].mean())
    print('\nAverage travel time; \nIn seconds: {} seconds. \nIn minutes: {} minutes.'.format(round(mean_traval_time), round(mean_traval_time/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
    print('\n')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('-'*40)
    print('Calculating User Stats...')
    print('-'*40)
    start_time = time.time()

    # Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print('Counts of user types:\n{}.'.format(count_of_user_types))

    # Display counts of gender
    if 'Gender' in df:
        count_of_gender = df['Gender'].value_counts()
        print('\nCounts of gender:\n{}.'.format(count_of_gender))
    else:
        print('\nThe \"Gender\" data for the chosen city is not available.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nyes: {}'.format(earliest_year, recent_year, common_year))
    else:
        print('\nThe \"Birth Year\" data for the chosen city is not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
    print('\n')

    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        user_inputs_message(city, month, day)
        display_5_raws(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
