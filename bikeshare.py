import time
import numpy as np
import pandas as pd

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Let\'s explore some US bikeshare data!')

    citychoice = 0
    monthchoice = 0
    daychoice = 0
    userchoice = 0
    cityoptions = {1:'Chicago', 2:'New York City', 3:'Washington'}
    monthoptions = {1:'January', 2:'February', 3:'March',
                    4:'April', 5:'May', 6:'June', 7:'July', 8:'August',
                    9:'September', 10:'October', 11:'November', 12:'December', 0:'all'}
    dayoptions = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday',
                    6:'Saturday', 7:'Sunday', 0:'all'}


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Enter the city you wish to select:")

    while True:
        userchoice = 0
        try:
            userchoice = int(input("1 for Chicago\n" + "2 for New York City\n" + "3 for Washington\n" + "0 to cancel : "))
        except ValueError:
            print("You need to enter a number value. Try again")
            continue
        else:
            if userchoice in cityoptions:
                print("Entry accepted")
                citychoice = userchoice
                break
            elif userchoice == 0:
                print("Goodbye.")
                exit()
            else:
                print("Sorry. You can't have that as a choice. Try again")
                continue

    print()
    print("You have chosen :",citychoice, "for the city which is {}".format(cityoptions[userchoice]))
    print()

    # get user input for month (all, january, february, ... , june)
    while True:
        userchoice = 0
        try:
            userchoice = int(input("Select the number of the month i.e. 1 for January, 2 for February, 3 for March etc. or 0 for all : "))
        except ValueError:
            print("You need to enter a number value. Try again")
            continue
        else:
            if userchoice in monthoptions:
                print("Entry accepted")
                monthchoice = userchoice
                break
            elif userchoice == 0:
                print("Entry accepted")
                monthchoice = userchoice
                break
            else:
                print("Sorry. You can't have that as a choice. Try again")
                continue

    print()
    print("You have chosen :",monthchoice, "for the month which is {}".format(monthoptions[userchoice]))
    print()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        userchoice = 0
        try:
            userchoice = int(input("Select the number of the day i.e. 1 for Monday, 2 for Tuesday etc. or 0 for all : "))
        except ValueError:
            print("You need to enter a number value. Try again")
            continue
        else:
            if userchoice in dayoptions:
                print("Entry accepted")
                daychoice = userchoice
                break
            elif userchoice == 0:
                print("Entry accepted")
                daychoice = userchoice
                break
            else:
                print("Sorry. You can't have that as a choice. Try again")
                continue

    print()
    print("You have chosen :",daychoice, "for the day which is {}".format(dayoptions[userchoice]))
    print()

    print('-'*40)

    city = cityoptions[citychoice].lower()
    month = monthoptions[monthchoice]
    day = dayoptions[daychoice]

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
    filename = city+".csv"
    df = pd.read_csv(filename)

    # Ask the user if they want to display the selected raw data on the screen.....
    while True:
        user_showdata = 0
        try:
            user_showdata = str(input("Would you like to include all of the selected data on the screen (yes/no)? "))
        except ValueError:
            print("You need to enter either 'yes' or 'no'. Try again")
            continue
        else:
            if user_showdata.lower() == "yes" or user_showdata.lower() == "no":
                print("Ok")
                break
            else:
                print("Incorrect choice. Enter yes or no")
                continue

    # Ask whether the user want to use the full dataset or just a given amount from the head or tail of the dataset.
    while True:
        try:
            developer_mode_value = input("Use full dataset or n header or tail rows? (f/h/t)")
        except ValueError:
            print("You need to enter a number value. Try again")
            continue
        else:
            if developer_mode_value.lower() == 'f':
                df = pd.DataFrame(df)
                break
            elif developer_mode_value.lower() == 'h':
                header_value = int(input("Enter number of header rows : "))
                df = pd.DataFrame(df.head(header_value))
                break
            elif developer_mode_value.lower() == 't':
                tail_value = int(input("Enter number of header rows : "))
                df = pd.DataFrame(df.tail(tail_value))
                break

            else:
                print("Incorrect choice. Enter f, h or t")
                continue


    # If a particular month or day of the week is selected, filter the data accordingly and re-create the df dataframe.
    if month != "all" or day != "all":
        if month != "all":
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['month'] = df['Start Time'].dt.month_name()
            df = df[df['month']==(month)]
        if day != "all":
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['day'] = df['Start Time'].dt.day_name()
            df = df[df['day']==(day)]

    # If the user has selected the data to be displayed, allow the user to scroll through 5 lines at a time
    # They are able to quit the scroll if it is a very large dataset and they don't want to scroll through all of it.
    if user_showdata.lower() =='yes':
        row_c = df.shape[0]
        if row_c > 5:
            print("There are {} rows collected from your selection so scrolling through 5 rows at a time".format(row_c))
            i = 0
            for i in range(i,row_c,5):
                    print(df.iloc[i:i+5, 1:9])
                    scroll_choice = input("Next 5 rows? Press any key to continue or q to quit?")
                    if scroll_choice == 'q':
                        break
                    else:
                        continue
        else:
            print(df.iloc[:, 1:9])      # Display the columns but not include the ones that will be used as filters later.

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    """
    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        Nil

    Locals:
        df_start - Pandas Dataframe containing start station and number of trips from there.
        df_highest_start_station - Pandas Dataframe taken from df_start Dataframe with
                    the station containing the highest number of starts.
        df_end - Pandas Dataframe containing destination station and the number of trips from there.
        df_highest_end_station - Pandas Dataframe taken from df_end Dataframe with the
                    station containing the highes number of trips ending there.
        df_combo - Pandas Dataframe containing a combination of start and end stations to calculate
                    the trip combinations with the greatest number of trips between them.
        df_hightest_combo - Pandas Dataframe containing the combined start and end stations with
                    the highest number of trips between them.
        (int) start_max_value, end_max_value, combo_max_value - temporary stores for the max values.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    df_start = pd.DataFrame(df.groupby(['Start Station']).size(), columns=["Trip Starts"])

    if df_start.empty:
        print("There is no data your selection")
        print("Please try again with a wider range if you selected particular months and days")
        return()

    start_max_value = df_start['Trip Starts'].max()
    #print("The start stations with the highest number of returns are:\n\n", df_start_max_value)
    print("The start stations with the highest number of returns are:")

    df_highest_start_station = df_start[df_start['Trip Starts']==start_max_value]
    print(df_highest_start_station)

    ##############################
    print("\n")

    # display most commonly used end station
    df_end = pd.DataFrame(df.groupby(['End Station']).size(), columns=["Trip Destinations"])

    end_max_value = df_end['Trip Destinations'].max()
    #print("The destination stations with the highest number of returns are:\n\n", df_end_max_value)
    print("The destination stations with the highest number of returns are:")

    df_highest_end_station = df_end[df_end['Trip Destinations']==end_max_value]
    print(df_highest_end_station)

    ###############################
    print("\n")

    # display most frequent combination of start station and end station trip
    df_combo = pd.DataFrame(df, columns = ['Start Station', 'End Station'])
    df_combo = pd.DataFrame(df_combo.groupby(['Start Station', 'End Station']).size(), columns=["Trips"])
    combo_max_value = df_combo['Trips'].max()

    #print("The trip combinations with the highest number of returns are:\n\n",  df_combo_max_value)
    print("The trip combinations with the highest number of returns are:")

    df_highest_combo = df_combo[df_combo['Trips'] == combo_max_value]
    print(df_highest_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press any key for next section of data.....")

def user_stats(df):
    """Displays statistics on bikeshare users."""

    """
    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        Nil

    Locals:
        df_user_type_count - Pandas Dataframe initially containing a single column for subscriber/customer
                    types which is processed with groupby into two rows later in the function with totals column added.
        df_gender_count - Pandas Dataframe like df_user_type_count containing a single column for male/female
                    entries which is processed with groupby into two rows later in the function with totals column added.
        df_birth - Pandas Dataframe taken from the selected dataframe and contains a single column with the birth year
                    entries taken from it
        df_birth_count - Pandas Dataframe taken from the df_birth dataframe and contains two columns with year and total
                    number of occurrances for that year.

        (int) user_type_nan, gender_nan, - temporary stores for the number of NaN values for user_type.
        (int) birth_youngest, birth_oldest - integer values for the youngest and oldest person in dataset.
        (int) birth_common_value - stores the number of the most common birth year occurrances.
        (int) common_birth_year - Pandas Series with the value of the most common birth year.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Check to see if we have any data to work with first.....
    if df.empty:
        print("There is no data for your selected timeframe. Please try again with a different selection.")
        return

    # Display counts of user types

    # Check to see if we have any data to display in that column first.
    df_user_type_count = pd.DataFrame(df, columns = ['User Type']).dropna(axis=0)
    if df_user_type_count.empty:
        print("There is no data in the table for user type information")
        print()
    else:
        # If we have data then redo the df_user_type_count but include any NaN values this time.
        df_user_type_count = pd.DataFrame(df, columns = ['User Type'])      # Create the dataframe of User Type count including NaNs.
        user_type_nan = df_user_type_count.isnull().sum().sum()             # Calculate the amount of any NaN values in the selected dataset.

        # Redo the user type count but drop any NaNs.
        df_user_type_count = pd.DataFrame(df, columns = ['User Type']).dropna(axis=0)
        df_user_type_count = pd.DataFrame(df_user_type_count.groupby(['User Type']).size(), columns=["Totals"]) # Group the user types and total up.

        # Display the results.
        print("The breakdown of users were:\n\nSubscribers...\n\n", df_user_type_count)
        print("There were {} people for who there is no user type information.".format(user_type_nan)) # Show how many nil values as a format.
        print()
        print()

    # Display counts of gender

    # Check to see if we have data to display in that column first.
    df_gender_count = pd.DataFrame(df, columns = ['Gender']).dropna(axis=0)
    if df_gender_count.empty:
        print("There is no data in the table for gender information")
        print()
    else:
        # If we have data then redo the df_gender_count but include any NaN values this time.
        df_gender_count = pd.DataFrame(df, columns = ['Gender'])        # Create the dataframe of gender count including NaNs.
        gender_nan = df_gender_count.isnull().sum().sum()                # Calculate the amount of any NaN values in the selected dataset.

        # Redo the dataframe for gender count but drop any NaNs.
        df_gender_count = pd.DataFrame(df, columns = ['Gender']).dropna(axis=0)
        df_gender_count = pd.DataFrame(df_gender_count.groupby(['Gender']).size(), columns=["Totals"])  # Group the genders and total them up.

        # Display the dataframe giving the gender and numbers.
        print("Genders...\n",df_gender_count)
        print("There were {} people who hadn't given their gender.".format(gender_nan))     # Show how many nil values as a format
        print()

    # Display earliest, most recent, and most common year of birth

    # Check to see if we have data to display in that column first.
    df_birth = pd.DataFrame(df, columns = ['Birth Year']).dropna(axis=0)
    if df_birth.empty:
        print("There is no data in the table for year of birth")
        print()
    else:
        # We can obtain the min and max values from the existing df dataframe.
        birth_youngest = df['Birth Year'].max()                  # Get the max value for the youngest birth.
        birth_oldest = df['Birth Year'].min()                    # Get the min value for the oldest birth.

        # Get the dataframe for list of births.
        df_birth = pd.DataFrame(df, columns = ['Birth Year'])               # Create df_birth dataframe for Birth Year
        df_birth_count = pd.DataFrame(df_birth.groupby(['Birth Year']).size(), columns=["Totals"]).reset_index() # and the grouped totals.

        # Get the highest value of occurrances for the year.
        birth_common_value = df_birth_count['Totals'].max()                 # Store the value of the highest number of occurrances.
        common_birth_year = df_birth_count[df_birth_count['Totals']==birth_common_value]['Birth Year'] # Compare this with the associated year.

        # Display the results.
        print("The youngest hirers were born in {}".format(int(birth_youngest)) )
        print("The oldest hirers were born in {}".format(int(birth_oldest)) )
        print("The most common year for births is {} with {} people born in that year".format(int(common_birth_year), birth_common_value))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

        input("Press any key for next section of data.....")

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    """
    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        Nil

    Locals:
        df_pop_month - Pandas Dataframe taken from the supplied dataframe selection with the month name as an index
                    and a totals column for the number of occurrances per month.
        df_busiest_month - Pandas Dataframe taken from the df_pop_month dataframe and contains the most popular month as
                    the index value and hire count value as a column.

        df_pop_day - Pandas Dataframe taken from the supplied dataframe selection with the day name as an index and
                    a totals column for the number of occurrances for that day.
        df_busiest_day - Pandas Dataframe taken from df_pop_day dataframe and contains the most popular day as
                    the index value and hire count value as a column.

        df_pop_start_hour - Pandas Dataframe taken from the supplied dataframe selection with the hour value as an index and
                    a totals column for the number of occurrances for that hour.
        df_busiest_start - Pandas Dataframe taken from df_pop_day dataframe and contains the most popular hour as
                    the index value and hire count value as a column.

        (int) pop_month_max_value - temporary store for the max value for the most popular month.
        (int) pop_day_max_value - temporary store for the max value for the most popular day.
        (int) pop_start_hour_max_value - temporary store for the max value for the start of trips.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month_name()

    # extract day from the Start Time column to create a day-of-the-week column
    df['day'] = df['Start Time'].dt.day_name()

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    if df.empty:
        print("There is no data for your selection.")
        print("If you have chosen specific months and days, please try a wider timeframe.")
    else:
        # display the most common month
        print("\n")

        df_pop_month = pd.DataFrame(df.groupby(['month']).size(), columns=["Hire Count"])

        pop_month_max_value = df_pop_month['Hire Count'].max()
        df_busiest_month = df_pop_month[df_pop_month['Hire Count']==pop_month_max_value]
        print("The most popular month to hire with the number of hires: \n", df_busiest_month)

        # display the most common day of week
        print('-'*20)
        print("\n")

        df_pop_day = pd.DataFrame(df.groupby(['day']).size(), columns=["Hire Count"])

        pop_day_max_value = df_pop_day['Hire Count'].max()
        df_busiest_day = df_pop_day[df_pop_day['Hire Count']==pop_day_max_value]
        print("The most popular day to hire with the number of hires: \n", df_busiest_day)

        # display the most common start hour
        print('-'*20)
        print("\n")

        df_pop_start_hour = pd.DataFrame(df.groupby(['hour']).size(), columns=["Hire Count"])

        pop_start_hour_max_value = df_pop_start_hour['Hire Count'].max()
        df_busiest_start = df_pop_start_hour[df_pop_start_hour['Hire Count']==pop_start_hour_max_value]
        print("The most popular hour to hire with the number of hires: \n ",df_busiest_start)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press any key for next section of data.....")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    """
    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    Returns:
        Nil

    Locals:
        (int) total_travel - temporary store for total number of seconds counted across all trip durations for selected timeframe.
        (int) mean_travel - temporary store for the average trip duration from all durations for the selected timeframe.
    """


    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df.groupby(['Trip Duration'])["Trip Duration"].sum().sum()

    if total_travel == 0:
        print("There is no data for your selection to display total travel information.")
        print()
    else:
        print("The total duration for the period is: {} seconds or {} mintues.".format(int(total_travel), format((total_travel/60), '.2f')))

    # display mean travel time
    mean_travel = pd.DataFrame(df, columns = ['Trip Duration']).dropna(axis=0)
    if mean_travel.empty:
        print("There is no data for your selection to display average travel times.")
        print()
    else:
        mean_travel = df.groupby(['Trip Duration'])["Trip Duration"].sum().mean()
        print("The mean trip duration for this period is: {} seconds or {} minutes.".format(int(mean_travel), format((mean_travel/60), '.2F')))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press any key for next section of data.....")

def main():

    # Display the chosen filters to the user.
    while True:
        city, month, day = get_filters()
        print("City choice is :", city.title())
        print("Month choice is :", month.title())
        print("Day choice is :", day.title())

        df = load_data(city, month, day)

        # Create a menu so the user can select individual statistics rather than the whole lot at once.
        while True:
            try:
                print()
                print("Select from the menu options below.")
                print("-"*35)
                print("1. Time statistics")
                print("2. Station statistics")
                print("3. Trip duration statistics")
                print("4. User statistics")
                print("0. Quit this menu")
                print()
                menu_choice = input("Choose an option:")
            except ValueError:
                print("You need to enter either 'yes' or 'no'. Try again")
                continue
            else:
                if menu_choice == '1':
                    time_stats(df)
                elif menu_choice == '2':
                    station_stats(df)
                elif menu_choice == '3':
                    trip_duration_stats(df)
                elif menu_choice == '4':
                    user_stats(df)
                elif menu_choice == '0':
                    break

        # Ask whether the user wants to start again from the start or quit the script.
        while True:
            try:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
            except ValueError:
                print("You need to enter either 'yes' or 'no'. Try again")
                continue
            else:
                if restart.lower() == 'yes':
                    break
                elif restart.lower() == 'no':
                    print("Ok. Thank you and goodbye.")
                    return
                else:
                    print("Sorry. You can't have that as a choice. Try again")
                    continue



def greeting():
    """Displays an initial greeting to the user based on the time of day."""

    """
        Args:
            Nil

        Returns:
            Nil

        Locals:
            (str) curr_hour - temporary store for the current hour value.
    """

    curr_hour = time.strftime('%H')
    if int(curr_hour) < 12 :
        period_of_day = "morning"
    elif int(curr_hour) >= 12 and int(curr_hour) < 18:
        period_of_day = "afternoon"
    elif int(curr_hour) > 17 :
        period_of_day = "evening"
    print ("Good " + period_of_day + "!")


if __name__ == "__main__":
    greeting()            ## Carry out initial greeting.

    main()
