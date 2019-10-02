import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    print('We have bikeshare data available from Chicago, New York City and Washington.')
    city = ''
    while city[:8] not in ['chicago', 'new york', 'washingt']:
        city = input('Which city\'s data would you like to explore?: ').lower()

    # get user input for month (all, january, february, ... , june)
    # start with dictionary of month names and their index
    months = {}
    month = ''
    for i in range(1, 13):
        months[i] = datetime.date(2019, i, 1).strftime('%B')

    # get input from users as either month number, month name or as all
    # store month as integer where 0 is all and 1-12 is Jan-Dec
    while month not in months.keys() and month != 0:
        try:
            month = input('Which month are you interested in?: ')
            month = int(month)
        except ValueError:
            for k, v in months.items():
                if month.lower() == 'all':
                    month = 0
                    break
                elif v.lower()[:3] == str(month).lower()[:3]:
                    month = k
                    break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # start with dictionary of weekday names and their index
    # store day of week as integer where 0 is all and 1-7 is Mon-Sun
    days = {}
    day = ''
    for i in range(1, 8):
        days[i] = datetime.date(2019, 4, i).strftime('%A')
    # get input from users as either weekday number, weekday name or as all
    while day not in days.keys() and day != 0:
        try:
            day = input('Which day of the week\'s data would you like to view?: ')
            day = int(day)
        except ValueError:
            for k, v in days.items():
                if day.lower() == 'all':
                    day = 0
                    break
                elif v.lower()[:3] == str(day).lower()[:3]:
                    day = k
                    break

    print('-'*40)

    # Print a message to the user showing the input they entered.
    if month == 0 and day == 0:
        print('Great, returning data for {} for all months and all days'.format(city.title()))
    elif month == 0:
        print('Great, returning data for {} for {}s from all months'.format(city.title(), days[day]))
    elif day == 0:
        print('Great, returning data for {} from {} for all days'.format(city.title(), months[month]))
    else:
        print('Great, returning data for {} from {} for {}s'.format(city.title(), months[month], days[day]))
    return city, month, day


#def load_data(city, month, day):
#    """
#    Loads data for the specified city and filters by month and day if applicable.
#
#    Args:
#        (str) city - name of the city to analyze
#        (str) month - name of the month to filter by, or "all" to apply no month filter
#        (str) day - name of the day of week to filter by, or "all" to apply no day filter
#    Returns:
#        df - Pandas DataFrame containing city data filtered by month and day
#    """
#
#
#    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
#        df = load_data(city, month, day)
#
#        time_stats(df)
#        station_stats(df)
#        trip_duration_stats(df)
#        user_stats(df)
#
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
