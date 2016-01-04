# HouseSorting
Puts people into houses based on ranking.

### Example usage
`python hat.py [candidates file] [houses file] [house max capacity]`

> House max capacity can be set to number of candidates / number of houses

```
python hat.py candidates.csv house_leaders.csv 3                                           ~/chtle/Git/VSA-House-Choice-Voting 1
House Number:   0
House:          Cancer
Leader:         Huy Nguyen
Members: 3
                Annie Nguyen    Choice Rank: 0
                Austina Nguyen  Choice Rank: 0
                Christine Phan  Choice Rank: 0

House Number:   1
House:          Taurus
Leader:         Jenny Lai
Members: 2
                Khoa Doan       Choice Rank: 2
                Matthew Nguyen  Choice Rank: 1

House Number:   2
House:          Aries
Leader:         Violet Nguyen
Members: 3
                Charlie Le      Choice Rank: 0
                Khoa Truong     Choice Rank: 0
                Vi Nguyen       Choice Rank: 0

House Number:   3
House:          Scorpio
Leader:         Daniel Ngo
Members: 3
                Sharon Trang    Choice Rank: 0
                Derrick Nguyen  Choice Rank: 0
                Baotuan Nguyen  Choice Rank: 0

House Number:   4
House:          Sagittarius
Leader:         Kathy Nguyen
Members: 1
                Cathy Quach     Choice Rank: 0

House Number:   5
House:          Gemini
Leader:         Chi Nguyen
Members: 3
                Jonathan Lai    Choice Rank: 0
                Ryan Le         Choice Rank: 0
                Kevin Hoang     Choice Rank: 0

```

Candidates.csv
- _name_: Name of people who are interested in being placed into a house.
- _choices_: Space separated string of house ids that are ranked in order of preference.
```
name,choices
Charlie Le,2 5 3 4 0 1
Austina Nguyen,0 1 2 3 4 5
Annie Nguyen,0 3 5 1 2 4
Jonathan Lai,5 4 3 2 1 0
Khoa Truong,2 5 4 1 0 3
Kevin Hoang,5 3 0 1 2 4
Christine Phan,0 5 3 1 4 2
Baotuan Nguyen,3 5 2 1 4 0
Ryan Le,5 2 0 1 3 4
Cathy Quach,4 1 5 2 3 0
Vi Nguyen,2 3 1 5 0 4
Khoa Doan,3 5 1 2 0 4
Derrick Nguyen,3 1 4 0 2 5
Sharon Trang,3 4 1 0 5 2
Matthew Nguyen,0 1 5 2 3 4
```

House_Leaders.csv
- _id_: Unique id of the house. Used by candidate to specify ranking.
- <i>leader_name</i>: Name of the house's leader.
- <i>house_name</i>: Name of the house
```
id,leader_name,house_name
0,Huy Nguyen,Cancer
1,Jenny Lai,Taurus
2,Violet Nguyen,Aries
3,Daniel Ngo,Scorpio
4,Kathy Nguyen,Sagittarius
5,Chi Nguyen,Gemini
```
