def laplace_smoothing(numerator, denominator, alpha=1):
    return (numerator + alpha) / (denominator + 2 * alpha)
