# 1. Introduction
# 1.1. What is MOPS Power Control?

MOPS Power Control is an application that adjusts the transmitting power of Base Transceiver Station (BTS) and Mobile Station (MS) based on measurement reports of BTS and MS.

# 1.2.  Purposes of the MOPS Power Control

Main purposes of MOPS Power Control application are saving the power of MS, BTS and also increasing the quality of the network connection by reducing the interference of the network.

# 1.3. Features

MOPS Power Control offers some extra features, allowing the user to:
Override default configuration
Turn on/off handover algorithm
Create a log file for debugging purposes
HTTP communication
Plotter

To use extra features, additional flags provided at terminal launching are required. See Section 3.5. "Additional features" for details
# 2. Installation of MOPS Power Control

Before installing MOPS Power Control make sure that your operating system is Linux
# 2.1. System requirements

For the application to work correctly you should have Python 3.6.1 interpreter installed on your machine and Linux operating system.
# 2.2. Where to get MOPS Power Control?
https://bitbucket.org/pat049b/mops_power_control
# 2.3. Installation instructions

Download all the files from the link provided in the previous section. Unzip them all into one directory, shell command for unzipping:

    unzip <file name>.zip -d <directory>

If unzip library is not installed on your system, run:

    sudo apt-get install unzip.

Files being in another directory may cause the necessity to provide an absolute path to them.
No installation is required, the script is interpreted by shell built-in interpreter. The program can be run from the terminal.

# 2.3.1. Required libraries

Matplotlib - the library is required for grapher.py to draw charts. Installation can be run by:

    pip-python3 matplotlib
    or
    apt-get install python3-matplotlib

Requests -  required for the HTTP server. Installation instruction on http://docs.python-requests.org/en/master/

# 3. User interface
# 3.1. Introduction

By now you should have MOPS Power Control application ready to work on your computer. In the next chapters we will explore:
How to use basic MOPS Power Control features.
How to change the configuration of MOPS Power Control to set different rules for working algorithm

# 3.2. Start MOPS Power Control

You can start the MOPS Power Control application from your shell using the command:

cat input.txt | python pc.py

TIP
When starting MOPS Power Control it is possible to specify optional settings using a command line. See Section 3.5. "Additional features" for details

# 3.3. Input

The algorithm takes input through stdin. The required input line is structured this way:

XL    XX    XXXX    num1    num2

    Where:
    XL - indicates the direction of transmission (UL or DL)
    XX - BTS number (S0 for the current cell, N1-6 for neighbor)
    XXXX - Mobile station name (any string without special signs)
    Num1 - power level
    Num2 - quality level

# 3.3.1. Configuration

Algorithm has default configuration parameters:

    target:-75    --> Setting target power in dBm
    hister:3      --> histeresy threshold
    maxInc:8      --> Maximum power increase
    maxIncHist:1  --> Maximum power increase inside hysteresis area
    maxDec:4      --> Maximum power decrease
    maxDecHist:1  --> Maximum power decrease inside hysteresis area
    changeThresh:1--> Threshold of change
    maxMissing:3  --> Maximum number of missing signals before\ launching MaxPower mode
    window:8      --> Number of measurements included in calculations
    offset:3      --> Minimum difference between current cell power\ and neighbour
    minAmount:4   --> Minimum amount of measurements to start PC

These settings can be customized. The customization process is described in section                3.5. “Additional Features”.

# 3.4. Output

There are a few options for getting output. Script output is printed by default in standard output in a terminal:

    cat input.txt | python3 pc.py

    Loading default configuration
    DL    S0      MS222    NCH
    UL    S0      MS222    NCH


# 3.4.1. Printing the output to a file

Commands are always printed in the terminal, they can be also redirected to a file by using file_name at the end of a terminal command:

    cat input.txt | python pc.py > output.txt

# 3.4.2. Database


Measurement data is stored in the database directly, or through the HTTP server if one is set up. See section 3.5.5. “HTTP communication” for details.

# 3.4.3.Graphic output

There is a possibility to visualize measurement data for the specified mobile station, See section 3.5.4. “Plotter” for details.

# 3.5. Additional features

# 3.5.1. User configuration

User can override default configuration of an algorithm. To do so, the additional flag should be Flag: -c

    Invoke example:
    cat input.txt | python3 pc.py -h -c
    cat input.txt | python3 pc.py -c

Feature description: Overrides default configuration with one specified in conf.cfg file. Detailed information related to changing configurable parameters is included inside this file.

# 3.5.2. Handover

Handover algorithm:
Flag: -h

    Invoke example:
    cat input.txt | python3 pc.py -h -c
    cat input.txt | python3 pc.py -h

Feature description: When neighbor cell measurement received, the algorithm is comparing the signal power of S0 cell with signal power of neighbor. Sends HOBC (Handover Better Cell) signal if a handover is profitable.

# 3.5.3. Debugger

Flag: -d

    Invoke example:
    cat input.txt | python3 pc.py -d -h
    cat input.txt | python3 pc.py -d

Feature description: Creates log for debugging purposes in logdeb.txt. Debugger appends information to this file. In order to wipe logs out, manual deletion of file is required. Example log from one input line:

    Current input line  UL S0 MS776 -78 2
    Line correct
    Current power history [-78, -75, -70, -70, -78]
    Current quality history ['2', '2', '1', '1', '2']
    Consecutive missings 0
    Enough data to take an action
    Average power: -74.71
    Average quality:1.61
    Command sent: UL   S0 MS776  NCH

# 3.5.4. Plotter

Flag: none - plotter is a separate application, using data in a database to visualize the history of power levels downlink and uplink for certain mobile station in the specified time window.

    Invoke example:
    python3 grapher.py ‘2017-07-20 20:00’ ‘2017-07-21 22:00’ ‘MS111’

After the name of the script (grapher.py), two following dates are beginning and end of a time window.

    Date format: ‘YYYY-MM-DD HH:MiMi:SS.SsSsSs’, where:
    Y - year, M - month, D - day
    H - hour, Mi - minute, S - seconds, Ss - parts of a second

Provided dates accuracy does not matter.
The last parameter is the name of a mobile station to be displayed.

Plotter uses matplotlib library, which must be downloaded previously.

    Installation on Ubuntu/Debian systems can be executed by command:
    sudo apt-get install python3-matplotlib or
    pip-python3 matplotlib



# 3.5.5 HTTP communication

To establish Http server user needs to launch it before launching a whole application.

    Steps to do that:
    1)Go to the project directory
    2)Launch http_server.py in python3 interpreter in the separate console by command:
    python3 http_server.py
    3)Now your server is working in a separate console.
    4)Run your program in another console and communication with HTTP in the server is established now. If you skip steps 1-3 your program is sending data to the database directly.

It may happen that your environment doesn’t have requests lib which is necessary for properly working HTTP communication. To get requests lib please find attached docs website: http://docs.python-requests.org/en/master/

# 3.5.6 Parser to analyze TCPDUMP

Flag: none - parser is a separate application, using data from tcpdump application to visualize the history of communication with the HTTP server.

    Steps to start:
    Start HTTP server - see 9.6 HTTP communication
    Start a new terminal

    Invoke example:
    tcpdump -A -v -i <interface> > <file_name>
    python3 ana.py <file_name>

