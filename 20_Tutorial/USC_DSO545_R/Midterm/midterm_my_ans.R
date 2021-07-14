setwd("/data/daveting/other_project/usc_dso_545/midterm")

library(dplyr)
library(ggplot2)

# Case 1

df = read.csv('hotdog.csv')

df %>% 
  ggplot(aes(x=Year, y=Dogs.eaten, fill=factor(New.record))) + 
  geom_col() + 
  scale_fill_manual(values = c("lightblue", "red")) + 
  theme(legend.position = "none") + 
  labs(title="Number of Hot Dogs Eaten", y="")


# Case 2

df = read.csv("gss.csv")

# Q1
q1 = df %>% 
  group_by(partyid) %>%
  summarise(cnt = n()) %>%
  filter(cnt >= 2000)

# Q2
q1 %>% 
  mutate(pct = cnt / sum(cnt)) %>%
  ggplot(aes(x=reorder(partyid, -pct), y=pct, fill=partyid)) +
  geom_col() + 
  scale_fill_manual(values = c("purple", "purple", "lightblue", "red", "lightblue", "red")) + 
  theme(legend.position = "none") + 
  labs(x="", y="Percentage (%)")

# Q3
df %>% 
  filter(!is.na(df$age), df$race %in% c("White", "Black")) %>%
  ggplot(aes(x=age, fill=race)) + 
  geom_density(alpha=0.4, color="white") + 
  labs(x="Age")

# Q4
df %>% 
  filter(!is.na(df$age)) %>% 
  mutate(age_group = (age >= 50)) %>% 
  ggplot(aes(x=partyid, fill=age_group)) +
  geom_bar(position="dodge") + 
  coord_flip() + 
  scale_fill_manual(values = c("lightblue", "pink")) + 
  theme(legend.position = "none") + 
  labs(title="Number of People: Party Aff. vs. Age (<50: Blue, >=50: Pink)", x="", y="")

# Q5
df %>% 
  filter(!is.na(tvhours)) %>%
  group_by(relig) %>%
  summarise(avg = mean(tvhours)) %>%
  ggplot(aes(y=reorder(relig, avg), x=avg)) +
  geom_point() + 
  labs(x="Avg. TV Hours", y="Religion")
  