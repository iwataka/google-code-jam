import qualified Control.Monad as Monad
import qualified Data.Maybe    as Maybe
import qualified Data.Set      as Set

splitIntoRanges l = let gaps = extractGaps (zip [0..] l)
                        gaps' = 0 : gaps ++ [length l - 1]
                     in listToRanges gaps'

listToRanges []             = []
listToRanges (a : c : rest) = (a, c) : listToRanges rest

extractGaps [] = []
extractGaps [_] = []
extractGaps ((a, b) : (c, d) : rest)
  | b == d = extractGaps ((c, d) : rest)
  | otherwise = a : c : extractGaps ((c, d) : rest)

mergeTwoRanges (s1, e1) (s2, e2) = (min s1 s2, max e1 e2)

spanMergeable (s, e) rs = let (mergeables, usedAfter) = span ((< e) . snd) rs
                              mergeables' = takeWhile ((<= e + 1) . fst) usedAfter
                           in (mergeables ++ mergeables', usedAfter)

merge' r rs = let (mergeables, usedAfter) = spanMergeable r rs
               in (map (mergeTwoRanges r) mergeables, usedAfter)

merge [] rs = []
merge (r : rest) rs = let (mergedRanges, usedAfter) = merge' r rs
                       in mergedRanges ++ merge rest usedAfter

size (start, end) = end - start + 1

solve ms ns = let mRanges = splitIntoRanges ms
                  nRanges = splitIntoRanges ns
                  mergedRanges = merge mRanges nRanges
                  maxSize = maximum $ map size mergedRanges
                  count = Set.size $ Set.fromList $ filter ((== maxSize) . size) mergedRanges
               in (maxSize, count)

readSignLine = do
    [d, a, b] <- words <$> getLine
    return (read d + read a, read d - read b)

readSignLines n = unzip <$> Monad.replicateM n readSignLine

readTestCase = getLine >>= readSignLines . read

main = do
    nTests <- read <$> getLine
    Monad.forM_ [1..nTests] $ \i -> do
        (ms, ns) <- readTestCase
        let (maxSize, count) = solve ms ns
        putStr $ "Case #" ++ show i ++ ": " ++ show maxSize ++ " " ++ show count ++ "\n"
