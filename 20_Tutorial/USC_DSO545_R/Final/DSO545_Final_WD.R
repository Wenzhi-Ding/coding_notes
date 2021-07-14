library(ggplot2)
library(dplyr)
library(lubridate)
library(stringr)
library(maps)
library(mapproj)

Sys.setlocale("LC_TIME", "English")

# Q1: d) list

# Q2: e) None of the above.
# Last row shinyApp(ui, server) is wrong. 
# It should not be in the server definition.

# Q3: b) ui

# Q4: d) str_detect

# Q5
pizzas = c("cheese","pepperoni", "sausage", "green peppers")
str_detect(pizzas, "pepper")

# Q6
currentvalue_cryptocurrency = c("55600,BIT", "3496,ETH", ".58,DOGE", "16.38,SUSHI", "152,ETC")
str_replace_all(str_extract(currentvalue_cryptocurrency, "\\d+.*\\d*"), ",", " ")

# Q7
lk = read.csv("C:\\Users\\Dave Ting\\Desktop\\lakersdata.csv")

lk$date_std = ymd(lk$date)
head(lk)

# Q8
lk$dow = wday(lk$date_std, label=TRUE)

lk %>% 
  group_by(dow) %>%
  ggplot(aes(x=dow)) + 
  geom_bar(width=0.2) +
  labs(x="Day of the Week", y="Count")

# Q9
# Unpaired two-samples t-test
t.test(filter(lk, game_type == "home")$points, filter(lk, game_type == "away")$points, 
       alternative = "two.sided", var.equal = FALSE)
# p-val=0.14
# No significant difference.

# Q10
un = read.csv("C:\\Users\\Dave Ting\\Desktop\\unicorn.csv")

un %>%
  group_by(Industry) %>%
  summarise(cnt=n()) %>%
  arrange(desc(cnt)) %>%
  top_n(9) %>%
  ggplot(aes(y=reorder(Industry, -cnt), x=cnt)) + 
  geom_bar(stat="identity") + 
  labs(x="Number of Unicorns", y="", title="Number of Unicorns by Industry")


# Q11
un$val = as.numeric(str_extract(un$Valuation, "\\d+"))
sum(filter(un, Industry == "Fintech")$val)
# 96


# Q12
un$year = as.factor(year(as_date(un$DateJoined, format="%m/%d/%Y")))

un %>%
  filter(Country %in% c("China", "India", "USA")) %>%
  ggplot(aes(fill=Country, x=year)) + 
  geom_bar(position="stack") +
  labs(x="", y="Number of Unicorns", title="Number of Unicorn Companies in China, India, and USA")


# Q13
map = map_data("world")
un$region = un$Country
tmp = un %>%
  filter(region %in% c("China", "India", "USA")) %>%
  group_by(region) %>%
  summarise(cnt=n())
df = left_join(map, tmp, by="region")

df %>%
  ggplot(aes(x=long, y=lat, group=group, fill=cnt)) +
  geom_polygon() + 
  scale_fill_gradient(low="white", high="darkred") +
  theme_void()


# Q14
some.en.countries = c("Portugal", "Spain", "France", "Switzerland", 
                      "Germany", "Belgium", "Norway", "Finland")

# Q15
some.eu.maps = map_data("world", region=some.en.countries)

# Q16
some.eu.maps %>%
  ggplot(aes(x=long, y=lat)) +
  geom_point()
summary(some.eu.maps$long)
summary(some.eu.maps$lat)

# Q17
rk = read.csv("C:\\Users\\Dave Ting\\Desktop\\rock.csv")

fit = lm(rk$area~rk$peri)
summary(fit)
# t = 9.808, very significant

# Q18
some.eu.maps %>%
  ggplot(aes(x=long, y=lat, group=group, fill=region)) +
  geom_polygon() + 
  scale_fill_viridis_d() +
  theme_void()

# Q19
states = map_data("state")

states %>% 
  top_n(6) %>%
  ggplot(aes(x=long, y=lat)) + 
  geom_point()

az = filter(states, region=="arizona")
head(az)

counties = map_data("county")
az_county = filter(counties, region=="arizona")

# Q20
az %>%
  ggplot(aes(x=long, y=lat, group=group)) +
  geom_polygon(colour="blue", fill=NA)


