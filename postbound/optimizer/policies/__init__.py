"""The policies module provides interfaces to parameterize different aspects of query optimization algorithms.

Policies differ from the abstract interfaces for each of the optimization stages in that the stages change the used
optimization algorithms. The policies change smaller details about those algorithms.

For example, optimization algorithms are often agnostic to specific cardinality estimation strategies. This module
provides abstract interfaces that allow the definition of different such estimation strategies. In turn, the
optimization algorithm can use a form of dependency injection to receive its cardinality estimation policy as an
argument instead of hard-coding the policy. This allows studying the effects of different cardinality estimators
on the overall optimization algorithm.
"""
