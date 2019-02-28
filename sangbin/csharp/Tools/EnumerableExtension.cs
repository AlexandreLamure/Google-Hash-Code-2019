using System;
using System.Collections.Generic;

namespace csharp.Tools
{
    public static class EnumerableExtension
    {
        public static void Apply<T>(this IEnumerable<T> collection, Action<T> handle)
        {
            if (collection == null) return;
            foreach (var item in collection)
            {
                handle(item);
            }
        }
    }
}
