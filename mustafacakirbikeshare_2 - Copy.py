import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['jan','feb','mar', 'apr', 'may', 'june','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('\n\nEnter city name, please select New York City, Chicago or Washington?\n\n').lower()
    while city not in CITY_DATA:
        print('Sorry that is not a valid input\n')
        city= input('\n\nAgain enter city name, please select New York City, Chicago or Washington?\n\n').lower()
    
        # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('\n\nYou select '+city.title()+' Now you should a month. Please select one at list Jan, Feb, Mar, Apr, May, June or All.\n\n').lower()
    while month not in MONTH_DATA:
        print('\n\nSorry that is not a valid input\n')
        month = input('\n\nPlease select one at list Jan, Feb, Mar, Apr, May, June or All.\n').lower()

   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    
    DAY_DATA = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day = input('\n\nYou select '+city.title()+' at '+month.title()+' Now you should a day. Please select one at list Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All.\n\n').lower()
    while day not in DAY_DATA:
        print('Sorry that is not a valid input\n')
        day = input('\n\nPlease select one at list Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All.\n\n').lower()
        


    print('-'*40)
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
    # load data file
    df = pd.read_csv(CITY_DATA[city])
    
     # convert date   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month

    if month != 'all':
        month = MONTH_DATA.index(month) +1
        df = df[df['month'] == month]
    
    # filter by day
    if day != 'all':
        df = df[df['week_day'] == day.title()]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month 
    
    most_common_month_num = df['Start Time'].dt.month.mode()[0]
    print('The most popular month is {}'.format(most_common_month_num))
   
    # TO DO: display the most common day of week
    most_common_day_of_week = df['week_day'].mode()[0]
    print('The most popular day is {}'.format(most_common_day_of_week))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most popular starting hour is {}'.format(most_common_hour))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('\n\nThe most popular start station is {}'.format(most_common_start_station))



    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\n\nThe most popular end station is {}'.format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("\n\nThe most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))
    
    # popular_start_end = df.loc['Start Station':'End Station'].mode()[0:]
    # print('\n\nThe most popular trip is {}'.format(popular_start_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('\nThe total travel time was:{}'.format(total_travel))

    # TO DO: display mean travel time
    total_mean=df['Trip Duration'].mean()
    print('\nThe mean distance travelled was {}'.format(total_mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    try:  
    # TO DO: Display counts of user types
        print("Counts of user types:\n")
        user_counts = df['User Type'].value_counts()
    
    
    
    # total numbers of user types 
        for index, user_count in enumerate(user_counts):
            print("  {}: {}".format(user_counts.index[index], user_count))

        
    # TO DO: Display counts of gender
        print("\nCounts of gender:\n")
        gender_counts = df['Gender'].value_counts()

    
    # total numbers of genders 
        for index, gender_count   in enumerate(gender_counts):
            print("  {}: {}".format(gender_counts.index[index], gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('\n\nThe earliest of birth is {}'.format(earliest_year))
        most_recent_year = df['Birth Year'].max()
        print('\n\nThe most recent year of birth is {}'.format(most_recent_year))
        most_common_year = df['Birth Year'].mode()[0]
        print('\n\nThe most common year of birth is {}'.format(most_common_year))

    except Exception as e:
        print("Exception occurred: {}".format(e))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():    
                    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # data for view
        df = pd.read_csv(CITY_DATA[city])
        # a counter for first five line
        efe=0
        while True:
            fiveline = input('\nDo you want to view first five line for data? Please enter yes or no, \n')
            if fiveline.lower() == 'yes':
                    print(df[efe:efe+7])
                    efe +=7
            elif fiveline.lower() == 'no':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
