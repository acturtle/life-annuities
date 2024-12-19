from cashflower import variable
from input import assumption, policy
from settings import settings


@variable()
def survival_rate(t):
    if t == 0:
        return 1
    return survival_rate(t-1) * (1 - assumption["DEATH_PROB"])


@variable()
def actuarial_present_value(t):
    if t == settings["T_MAX_CALCULATION"]:
        return expected_payment(t)
    return expected_payment(t) + actuarial_present_value(t+1) * 1/(1+assumption["INTEREST_RATE"])


@variable()
def survival_rate(t):
    if t == 0:
        return 1
    return survival_rate(t-1) * (1 - assumption["DEATH_PROB"])


@variable()
def expected_payment(t):
    if t == 0 or t > policy.get("remaining_term"):
        return 0
    return survival_rate(t) * policy.get("payment")


@variable()
def actuarial_present_value(t):
    if t == settings["T_MAX_CALCULATION"]:
        return expected_payment(t)
    return expected_payment(t) + actuarial_present_value(t+1) * 1/(1+assumption["INTEREST_RATE"])
