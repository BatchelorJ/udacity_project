import time
import datetime
import pandas as pd
import numpy as np

city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user for input in selecting a city from predefined list, a month and a day
    :return city: lowercase string either 'chicago', 'new york' or 'washington'
    :return month: month of year (jan to june): integer in range 0 - 6 where 0 represents user selecting all months
    :return day: day of week: integer in range 0 - 7 where 0 represents user selecting all days of week, monday is 1
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    print('We have bikeshare data available from Chicago, New York City and Washington.')
    city = ''
    while city[:8] not in ['chicago', 'new york', 'washingt']:
        city = input('Which city\'s data would you like to explore?: ').lower()

    # tidy up user input
    if city[:8] == 'chicago':
        city = 'chicago'
    elif city[:8] == 'new york':
        city = 'new york city'
    elif city[:8] == 'washint':
        city = 'washington'

    # get user input for month (all, january, february, ... , june)
    # start with dictionary of month names and their index
    months = {}
    month = ''
    for i in range(1, 7):
        months[i] = datetime.date(2019, i, 1).strftime('%B')

    # get input from users as either month number, month name or as all
    # store month as integer where 0 is all and 1-12 is Jan-Dec
    while month not in months.keys() and month != 0:
        try:
            month = input('Which month (January to June) are you interested in? (enter all for all months): ')
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
            day = input('Which day of the week\'s data would you like to view? (enter all for all days): ')
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


def load_data(city, month=0, day=0):
    """
    Takes user-supplied inputs, reads in csv datasets to pandas dataframes and filters on parameters
    :param city: lowercase string either 'chicago', 'new york' or 'washington'
    :param month: month of year: integer in range 0 - 12 where 0 represents user selecting all months
    :param day: day of week: integer in range 0 - 7 where 0 represents user selecting all days of week
    :return:
    """

    # Specify source data depending on city input
    try:
        city_csv = city_data[city]
    except KeyError:
        raise NameError('no data available for city {}'.format(city))

    # create pandas dataframe from csv, rename columns and cast dates to Timestamp objects
    df = pd.read_csv('source_data\\{}'.format(city_csv))
    df = df.rename(columns={'Unnamed: 0': 'trip_id',
                            'Start Time': 'start_time',
                            'End Time': 'end_time',
                            'Trip Duration': 'trip_duration',
                            'Start Station': 'start_station',
                            'End Station': 'end_station',
                            'User Type': 'user_type',
                            'Gender': 'gender',
                            'Birth Year': 'birth_year'})
    df['start_time'] = pd.to_datetime(df['start_time'])
    df['end_time'] = pd.to_datetime(df['end_time'])

    # check for valid month and day inputs
    if not isinstance(month, int) and month not in range(0, 13):
        raise ValueError('invalid month value: must be integer between 0 and 12')
    elif not isinstance(day, int) and day not in range(0, 8):
        raise ValueError('invalid day value: must be integer between 0 and 7')

    # filter based on combination of day and month input
    if day == 0 and month == 0:
        pass
    elif month == 0:
        df = df[df['start_time'].dt.dayofweek == day - 1]
        pass
    elif day == 0:
        df = df[df['start_time'].dt.month == month]
        pass
    else:
        df = df[df['start_time'].dt.month == month]
        df = df[df['start_time'].dt.dayofweek == day - 1]

    return df


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

    # Calculate counts of user types
    if 'user_type' in df:
        user_counts = df['user_type'].dropna(axis=0).value_counts().rename('Count')
        user_percent = df['user_type'].dropna(axis=0).value_counts(normalize=True).rename('Percentage')
        df_user = pd.concat([user_counts, user_percent], axis=1)
        df_user['Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df_user['Percentage']],
                                          index=df_user.index)
        print('User Statistics by type of user\n' + '-'*40)
        print(df_user)
        print()

    else:
        print('Sorry, no user type data available for this city')

    # Calculate gender statistics
    if 'gender' in df:
        gender_counts = df['gender'].dropna(axis=0).value_counts().rename('Count')
        gender_percent = df['gender'].dropna(axis=0).value_counts(normalize=True).rename('Percentage')
        df_gender = pd.concat([gender_counts, gender_percent], axis=1)
        df_gender['Percentage'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df_gender['Percentage']],
                                            index=df_gender.index)
        print('\nGender Statistics\n' + '-'*40)
        print(df_gender)
        print()
    else:
        print('Sorry, no gender data available for this city')

    # Calculate earliest, most recent, and most common year of birth
    if 'birth_year' in df:
        youngest = int(df['birth_year'].dropna(axis=0).max())
        oldest = int(df['birth_year'].dropna(axis=0).min())
        commonest = int(df['birth_year'].dropna(axis=0).mode()[0])
        # TODO: print birth year
    else:
        print('Sorry, no birth year data available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
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
