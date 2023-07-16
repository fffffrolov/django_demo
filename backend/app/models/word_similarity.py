from typing import Union

from django.db.models import Field, Func, Lookup, QuerySet, Value, fields


class WordSimilarity(Func):
    """
    Get PostgreSQL word_similarity between given string and field or expression.
    Example of use: query.annotate(word_similarity=WordSimilarity(query_string, field))
    """
    function = 'word_similarity'
    template = '%(function)s(%(expressions)s)'

    def __init__(self, value: Union[Value, str], *expressions, output_field=None, **extra):
        if value is not Value:
            value = Value(value)
        if output_field is None:
            output_field = fields.FloatField()
        expressions = value, *expressions
        super().__init__(*expressions, output_field=output_field, **extra)


@Field.register_lookup
class WordSimilar(Lookup):
    """
    Get PostgreSQL word_similarity between given string and field or expression.
    Examples of use:
        query.filter(field__word_similar=query_string, field)
        query.filter(field__word_similar=(query_string, 0.9), field)
    """
    lookup_name = 'word_similar'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)

        min_similarity = 0.5
        if len(rhs_params) > 1:
            rhs_params, min_similarity = rhs_params
            assert 0 <= float(min_similarity) <= 1

        params = lhs_params + rhs_params

        return 'word_similarity(%s, %s) >= %s' % (rhs, lhs, min_similarity), params    # noqa MOD001


class WordSimilarityQuerySet(QuerySet):
    def with_word_similarity(self, field: str, query_string: str) -> QuerySet:
        return self.annotate(
            word_similarity=WordSimilarity(query_string, field),
        ).order_by('-word_similarity')
