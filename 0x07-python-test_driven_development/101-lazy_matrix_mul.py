#!/usr/bin/python3
"""
Defines a function that multiplies 2 matrices by using the module NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix that is given
    Args:
        m_a: input first matrix
        m_b: input second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
